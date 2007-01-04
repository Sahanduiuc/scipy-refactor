#include <Python.h>
#include <structmember.h>
#include <stdio.h>
#include <string.h>
#include "mxDateTime.h"
#include "arrayobject.h"

static char cseries_doc[] = "Speed sensitive time series operations";

///////////////////////////////////////////////////////////////////////


static //PyArrayObject *
setArrayItem_1D(PyArrayObject **theArray, long index, PyObject *newVal)
{
    if (index >= 0)
    {
        //set value in array
        PyArray_SETITEM(*theArray, PyArray_GetPtr(*theArray, &index), newVal);
    }

}

static //PyArrayObject *
setArrayItem_2D(PyArrayObject **theArray, long index_x, long index_y, PyObject *newVal)
{
    long idx[] = {index_x, index_y};

    if (index_x >= 0 && index_y >= 0) {
        //set value in array
        PyArray_SETITEM(*theArray, PyArray_GetPtr(*theArray, idx), newVal);
    }

}


static int
freqVal(char freq)
{
    switch(freq)
    {
        case 'A':
            //annual
            return 1;
        case 'Q':
            //quarterly
            return 2;
        case 'M':
            //monthly
            return 3;
        case 'B':
            //business
            return 4;
        case 'D':
            //daily
            return 5;
        default:
            return 0;
    }
}

static long
toDaily(long fromDate, char fromFreq)
{
    long absdate;
    int y,m,d;

    mxDateTimeObject *theDate;

    //convert fromDate to days since (0 AD - 1 day)
    switch(fromFreq)
    {
        case 'D':
            absdate = fromDate;
            break;
        case 'B':
            absdate = ((fromDate-1)/5)*7 + (fromDate-1)%5 + 1;
            break;
        case 'M':
            y = fromDate/12;
            m = fromDate%12;

            if (m == 0)
            {
                m = 12;
                y--;
            }
            d=1;
            break;
        case 'Q':
            y = fromDate/4;
            m = (fromDate%4) * 3 - 2;

            if (m < 1)
            {
                m += 12;
                y--;
            }
            else if (m == 12)
            {
                m = 1;
                y++;
            }
            d=1;
            break;
        case 'A':
            y = fromDate;
            m = 1;
            d = 1;
            break;
        default:
            return -1;
    }

    if (freqVal(fromFreq) < 4)
    {
        theDate = (mxDateTimeObject *)mxDateTime.DateTime_FromDateAndTime(y,m,d,0,0,0);
        absdate = (long)(theDate->absdate);
    }

    return absdate;

}


static long
getDateInfo_sub(long dateNum, char freq, char info) {

    long monthNum;
    mxDateTimeObject *convDate;
    convDate = (mxDateTimeObject *)mxDateTime.DateTime_FromAbsDateAndTime(toDaily(dateNum,freq),0);

    switch(info)
    {
        case 'Y': //year

            return (long)(convDate->year);

        case 'Q': //quarter
            monthNum = (long)(convDate->month);
            return ((monthNum-1)/3)+1;

        case 'M': //month
            return (long)(convDate->month);

        case 'D': //day
            return (long)(convDate->day);

        case 'W': //day of week
            return (long)(convDate->day_of_week);
        default:
            return -1;
    }
}


static char cseries_getDateInfo_doc[] = "";
static PyObject *
cseries_getDateInfo(PyObject *self, PyObject *args)
{
    char *freq;
    char *info;

    PyArrayObject *array;
    PyArrayObject *tempArray;
    PyArrayObject *newArray;

    char *getptr;
    PyObject *val;
    long i, lngVal, dInfo, dim;

    if (!PyArg_ParseTuple(args, "Oss:getDateInfo(array, freq, info)", &tempArray, &freq, &info)) return NULL;

    array = PyArray_GETCONTIGUOUS(tempArray);

    dim = array->dimensions[0];

    //initialize new array
    newArray = (PyArrayObject*)PyArray_SimpleNew(array->nd, &dim, array->descr->type_num);

    for (i = 0; i < array->dimensions[0]; i++)
    {
        getptr = array->data + i*array->strides[0];
        val = PyArray_GETITEM(array, getptr);
        lngVal = PyInt_AsLong(val);
        dInfo = getDateInfo_sub(lngVal, *freq, *info);

        setArrayItem_1D(&newArray, i, PyInt_FromLong(dInfo));
    }

    return (PyObject *) newArray;

}


/*
convert fromDate to a date at toFreq according to relation
*/
static long
asfreq(long fromDate, char fromFreq, char toFreq, char relation)
{
    long absdate, secsInDay;
    long converted;
    int y,m, doAfter;

    mxDateTimeObject *convDate;

    secsInDay = 86400;
    doAfter = 0;

    if (relation == 'A') {
        switch(fromFreq)
        {

            case 'D': //daily

                switch(toFreq)
                {
                    case 'A':
                        break;
                    case 'Q':
                        break;
                    case 'M':
                        break;
                    case 'B':
                        break;
                    default:
                        doAfter = 1;
                        break;
                }
                break;

            case 'B': //business

                switch(toFreq)
                {
                    case 'A':
                        break;
                    case 'Q':
                        break;
                    case 'M':
                        break;
                    case 'D':
                        break;
                    default:
                        doAfter = 1;
                        break;
                }
                break;

            case 'M': //monthly

                switch(toFreq)
                {
                    case 'A':
                        break;
                    case 'Q':
                        break;
                    default:
                        doAfter = 1;
                        break;
                }
                break;

            case 'Q': //quarterly

                switch(toFreq)
                {
                    case 'A':
                        break;
                    default:
                        doAfter = 1;
                        break;
                }
                break;

            case 'A': //annual
                doAfter = 1;
                break;

        }

    }

    if (doAfter) {
        absdate = toDaily(fromDate + 1, fromFreq);
    } else {
        absdate = toDaily(fromDate, fromFreq);
    }

    convDate = (mxDateTimeObject *)mxDateTime.DateTime_FromAbsDateAndTime(absdate,0);

    y = convDate->year;
    m = convDate->month;

    //convert convDate to appropriate # of periods according to toFreq
    switch(toFreq)
    {
        case 'D':
            converted = absdate;
            break;
        case 'B':
            if (convDate->day_of_week > 4) //is weekend day
            {
                if (fromFreq == 'D' && relation == 'B') {
                    //change to friday before weekend
                    absdate -= (convDate->day_of_week - 4);
                } else {
                    //change to Monday after weekend
                    absdate += (7 - convDate->day_of_week);
                }
            }
            //converted = (long)((absdate / 7 * 5.0) + absdate%7);
            converted = (long)((absdate / 7 * 5.0) + absdate%7);
            break;
        case 'M':
            converted = (long)(y*12 + m);
            break;
        case 'Q':
            converted = (long)(y*4 + ((m-1)/3) + 1);
            break;
        case 'A':
            converted = (long)(y);
            break;
        default:
            return -1;
    }

    if (doAfter) {
        return converted-1;
    } else {
        return converted;
    }
}


/*
for use internally by the convert function. Same as the asfreq function,
except going from daily to business returns -1 always if fromDate is on
a weekend
*/
static long
asfreq_forseries(long fromDate, char fromFreq, char toFreq, char relation)
{
    mxDateTimeObject *convDate;

    if (fromFreq == 'D' && toFreq == 'B') {
        convDate = (mxDateTimeObject *)mxDateTime.DateTime_FromAbsDateAndTime(fromDate,0);
        if (convDate->day_of_week > 4) //is weekend day
        {
                return -1;
        }
    }

    return asfreq(fromDate, fromFreq, toFreq, relation);
}

static int validFreq(char freq) {
    switch(freq)
    {
        case 'A':
            return 1;
        case 'Q':
            return 1;
        case 'M':
            return 1;
        case 'B':
            return 1;
        case 'D':
            return 1;
        default:
            return 0;
    }
}


static int
expand(long oldSize, char fromFreq, char toFreq, long *newLen, long *newHeight)
{

    int maxBusDaysPerYear, maxBusDaysPerQuarter, maxBusDaysPerMonth;
    int minBusDaysPerYear, minBusDaysPerQuarter, minBusDaysPerMonth;

    int maxDaysPerYear, maxDaysPerQuarter, maxDaysPerMonth;
    int minDaysPerYear, minDaysPerQuarter, minDaysPerMonth;

    minBusDaysPerYear = 260;    maxBusDaysPerYear = 262;
    minBusDaysPerQuarter = 64;  maxBusDaysPerQuarter = 66;
    minBusDaysPerMonth = 20;    maxBusDaysPerMonth = 23;

    minDaysPerYear = 365;       maxDaysPerYear = 366;
    minDaysPerQuarter = 90;     maxDaysPerQuarter = 92;
    minDaysPerMonth = 28;       maxDaysPerMonth = 31;

    if (!validFreq(fromFreq)) return 0;
    if (!validFreq(toFreq)) return 0;

    if (fromFreq == toFreq) {
        *newLen = oldSize;
        *newHeight = 1;
    } else {

        switch(fromFreq)
        {
            case 'A': //annual

                switch(toFreq)
                {
                    case 'Q':
                        *newLen = oldSize * 4;
                        *newHeight = 1;
                        break;
                    case 'M':
                        *newLen = oldSize * 12;
                        *newHeight = 1;
                        break;
                    case 'B':
                        *newLen = oldSize * maxBusDaysPerYear;
                        *newHeight = 1;
                        break;
                    case 'D':
                        *newLen = oldSize * maxDaysPerYear;
                        *newHeight = 1;
                        break;
                }
                break;

            case 'Q': //quarterly

                switch(toFreq)
                {
                    case 'A':
                        *newLen = (oldSize / 4) + 2;
                        *newHeight = 4;
                        break;
                    case 'M':
                        *newLen = oldSize * 3;
                        *newHeight = 1;
                        break;
                    case 'B':
                        *newLen = oldSize * maxBusDaysPerQuarter;
                        *newHeight = 1;
                        break;
                    case 'D':
                        *newLen = oldSize * maxDaysPerQuarter;
                        *newHeight = 1;
                        break;
                }
                break;

            case 'M': //monthly

                switch(toFreq)
                {
                    case 'A':
                        *newLen = (oldSize / 12) + 2;
                        *newHeight = 12;
                        break;
                    case 'Q':
                        *newLen = (oldSize / 3) + 2;
                        *newHeight = 3;
                        break;
                    case 'B':
                        *newLen = oldSize * maxBusDaysPerMonth;
                        *newHeight = 1;
                        break;
                    case 'D':
                        *newLen = oldSize * maxDaysPerMonth;
                        *newHeight = 1;
                        break;
                }
                break;

            case 'B': //business

                switch(toFreq)
                {
                    case 'A':
                        *newLen = (oldSize / minBusDaysPerYear) + 2;
                        *newHeight = maxBusDaysPerYear;
                        break;
                    case 'Q':
                        *newLen = (oldSize / minBusDaysPerQuarter) + 2;
                        *newHeight = maxBusDaysPerQuarter;
                        break;
                    case 'M':
                        *newLen = (oldSize / minBusDaysPerMonth) + 2;
                        *newHeight = maxBusDaysPerMonth;
                        break;
                    case 'D':
                        *newLen = ((7 * oldSize)/5) + 2;
                        *newHeight = 1;
                        break;
                }
                break;

            case 'D': //daily

                switch(toFreq)
                {
                    case 'A':
                        *newLen = (oldSize / minDaysPerYear) + 2;
                        *newHeight = maxDaysPerYear;
                        break;
                    case 'Q':
                        *newLen = (oldSize / minDaysPerQuarter) + 2;
                        *newHeight = maxDaysPerQuarter;
                        break;
                    case 'M':
                        *newLen = (oldSize / minDaysPerMonth) + 2;
                        *newHeight = maxDaysPerMonth;
                        break;
                    case 'B':
                        *newLen = ((5 * oldSize)/7) + 2;
                        *newHeight = 1;
                        break;                }
                break;
        }
    }

    return 1;

}


static char cseries_convert_doc[] = "";
static PyObject *
cseries_convert(PyObject *self, PyObject *args)
{
    PyArrayObject *array;
    PyArrayObject *tempArray;
    PyArrayObject *newArray;

    PyArrayObject *mask;
    PyArrayObject *tempMask;
    PyArrayObject *newMask;

    PyObject *returnVal = NULL;

    long startIndex, newStart, newStartYaxis;
    long newLen, newHeight;
    long i, currIndex, prevIndex;
    long nd;
    long *dim;
    long currPerLen;
    char *fromFreq, *toFreq, *position;
    char relation;

    PyObject *val, *valMask;

    int toFrVal, fromFrVal;

    returnVal = PyDict_New();

    if (!PyArg_ParseTuple(args, "OssslO:convert(array, fromfreq, tofreq, position, startIndex, mask)", &tempArray, &fromFreq, &toFreq, &position, &startIndex, &tempMask)) return NULL;

    if (toFreq[0] == fromFreq[0])
    {

        PyDict_SetItemString(returnVal, "values", (PyObject*)tempArray);
        PyDict_SetItemString(returnVal, "mask", (PyObject*)tempMask);

        return returnVal;
    }

    switch(position[0])
    {
        case 'S':
            // start -> before
            relation = 'B';
            break;
        case 'E':
            // end -> after
            relation = 'A';
            break;
        default:
            return NULL;
            break;
    }

    //get frequency numeric mapping
    fromFrVal = freqVal(fromFreq[0]);
    toFrVal = freqVal(toFreq[0]);

    array = PyArray_GETCONTIGUOUS(tempArray);
    mask = PyArray_GETCONTIGUOUS(tempMask);

    //expand size to fit new values if needed
    if (!expand(array->dimensions[0], fromFreq[0], toFreq[0], &newLen, &newHeight)) return NULL;

    //convert start index to new frequency
    newStart = asfreq(startIndex, fromFreq[0], toFreq[0], 'B');

    if (newHeight > 1) {

        newStartYaxis = startIndex - asfreq(newStart, toFreq[0], fromFreq[0], 'B');
        currPerLen = newStartYaxis;

        nd = 2;
        dim = malloc(nd * sizeof(int));
        dim[0] = newLen;
        dim[1] = newHeight;
    } else {
        currPerLen = 0;
        nd = 1;
        dim = malloc(nd * sizeof(int));
        dim[0] = newLen;
    }

    newArray = (PyArrayObject*)PyArray_SimpleNew(nd, dim, array->descr->type_num);
    newMask  = (PyArrayObject*)PyArray_SimpleNew(nd, dim, mask->descr->type_num);

    free(dim);

    PyArray_FILLWBYTE(newArray,0);
    PyArray_FILLWBYTE(newMask,1);

    //initialize prevIndex
    prevIndex = newStart;

    //set values in the new array
    for (i = 0; i < array->dimensions[0]; i++)
    {

        //get value from old array
        val = PyArray_GETITEM(array, PyArray_GetPtr(array, &i));

        //get the mask corresponding to the old value
        valMask = PyArray_GETITEM(mask, PyArray_GetPtr(mask, &i));

        //find index for start of current period in new frequency
        currIndex = asfreq_forseries(startIndex + i, fromFreq[0], toFreq[0], relation);


        if (newHeight > 1) {

                if (currIndex != prevIndex)
                {
                    //reset period length
                    currPerLen = 0;
                    prevIndex = currIndex;
                }

                //set value in the new array
                setArrayItem_2D(&newArray, currIndex-newStart, currPerLen, val);
                setArrayItem_2D(&newMask, currIndex-newStart, currPerLen, valMask);

                currPerLen++;

        } else {

            setArrayItem_1D(&newArray, currIndex-newStart, val);
            setArrayItem_1D(&newMask, currIndex-newStart, valMask);

        }

    }

    PyDict_SetItemString(returnVal, "values", (PyObject*)newArray);
    PyDict_SetItemString(returnVal, "mask", (PyObject*)newMask);

    return returnVal;

}


static char cseries_asfreq_doc[] = "";
static PyObject *
cseries_asfreq(PyObject *self, PyObject *args)
{
    PyArrayObject *fromDates, *toDates;
    PyArrayIterObject *iterFrom, *iterTo;
    PyObject *fromDateObj, *toDateObj;
    char *fromFreq, *toFreq, *relation;
    long fromDate, toDate;

    if (!PyArg_ParseTuple(args, "Osss:asfreq(fromDates, fromfreq, tofreq, relation)", &fromDates, &fromFreq, &toFreq, &relation)) return NULL;

    toDates = (PyArrayObject *)PyArray_Copy(fromDates);

    iterFrom = (PyArrayIterObject *)PyArray_IterNew((PyObject *)fromDates);
    if (iterFrom == NULL) return NULL;

    iterTo = (PyArrayIterObject *)PyArray_IterNew((PyObject *)toDates);
    if (iterTo == NULL) return NULL;

    while (iterFrom->index < iterFrom->size) {

        fromDateObj = PyArray_GETITEM(fromDates, iterFrom->dataptr);
        fromDate = PyInt_AsLong(fromDateObj);
        toDate = asfreq(fromDate, fromFreq[0], toFreq[0], relation[0]);
        toDateObj = PyInt_FromLong(toDate);

        PyArray_SETITEM(toDates, iterTo->dataptr, toDateObj);

        PyArray_ITER_NEXT(iterFrom);
        PyArray_ITER_NEXT(iterTo);
    }

    return (PyObject *)toDates;

}


///////////////////////////////////////////////////////////////////////

static PyMethodDef cseries_methods[] = {
    {"convert", cseries_convert, METH_VARARGS, cseries_convert_doc},
    {"asfreq", cseries_asfreq, METH_VARARGS, cseries_asfreq_doc},
    {"getDateInfo", cseries_getDateInfo, METH_VARARGS, cseries_getDateInfo_doc},
    {NULL, NULL}
};

PyMODINIT_FUNC
initcseries(void)
{
    Py_InitModule3("cseries", cseries_methods, cseries_doc);
    mxDateTime_ImportModuleAndAPI();
    import_array();
}
# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.34
#
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _sparsetools
import new
new_instancemethod = new.instancemethod
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'PySwigObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types



def expandptr(*args):
  """expandptr(int n_row, int Ap, int Bi)"""
  return _sparsetools.expandptr(*args)

def csr_count_blocks(*args):
  """csr_count_blocks(int n_row, int n_col, int R, int C, int Ap, int Aj) -> int"""
  return _sparsetools.csr_count_blocks(*args)

def csr_matmat_pass1(*args):
  """
    csr_matmat_pass1(int n_row, int n_col, int Ap, int Aj, int Bp, int Bj, 
        int Cp)
    """
  return _sparsetools.csr_matmat_pass1(*args)

def csc_matmat_pass1(*args):
  """
    csc_matmat_pass1(int n_row, int n_col, int Ap, int Ai, int Bp, int Bi, 
        int Cp)
    """
  return _sparsetools.csc_matmat_pass1(*args)

def csr_has_sorted_indices(*args):
  """csr_has_sorted_indices(int n_row, int Ap, int Aj) -> bool"""
  return _sparsetools.csr_has_sorted_indices(*args)


def csr_diagonal(*args):
  """
    csr_diagonal(int n_row, int n_col, int Ap, int Aj, signed char Ax, 
        signed char Yx)
    csr_diagonal(int n_row, int n_col, int Ap, int Aj, unsigned char Ax, 
        unsigned char Yx)
    csr_diagonal(int n_row, int n_col, int Ap, int Aj, short Ax, short Yx)
    csr_diagonal(int n_row, int n_col, int Ap, int Aj, int Ax, int Yx)
    csr_diagonal(int n_row, int n_col, int Ap, int Aj, long long Ax, 
        long long Yx)
    csr_diagonal(int n_row, int n_col, int Ap, int Aj, float Ax, float Yx)
    csr_diagonal(int n_row, int n_col, int Ap, int Aj, double Ax, double Yx)
    csr_diagonal(int n_row, int n_col, int Ap, int Aj, npy_cfloat_wrapper Ax, 
        npy_cfloat_wrapper Yx)
    csr_diagonal(int n_row, int n_col, int Ap, int Aj, npy_cdouble_wrapper Ax, 
        npy_cdouble_wrapper Yx)
    """
  return _sparsetools.csr_diagonal(*args)

def csc_diagonal(*args):
  """
    csc_diagonal(int n_row, int n_col, int Ap, int Aj, signed char Ax, 
        signed char Yx)
    csc_diagonal(int n_row, int n_col, int Ap, int Aj, unsigned char Ax, 
        unsigned char Yx)
    csc_diagonal(int n_row, int n_col, int Ap, int Aj, short Ax, short Yx)
    csc_diagonal(int n_row, int n_col, int Ap, int Aj, int Ax, int Yx)
    csc_diagonal(int n_row, int n_col, int Ap, int Aj, long long Ax, 
        long long Yx)
    csc_diagonal(int n_row, int n_col, int Ap, int Aj, float Ax, float Yx)
    csc_diagonal(int n_row, int n_col, int Ap, int Aj, double Ax, double Yx)
    csc_diagonal(int n_row, int n_col, int Ap, int Aj, npy_cfloat_wrapper Ax, 
        npy_cfloat_wrapper Yx)
    csc_diagonal(int n_row, int n_col, int Ap, int Aj, npy_cdouble_wrapper Ax, 
        npy_cdouble_wrapper Yx)
    """
  return _sparsetools.csc_diagonal(*args)

def csr_tocsc(*args):
  """
    csr_tocsc(int n_row, int n_col, int Ap, int Aj, signed char Ax, 
        int Bp, int Bi, signed char Bx)
    csr_tocsc(int n_row, int n_col, int Ap, int Aj, unsigned char Ax, 
        int Bp, int Bi, unsigned char Bx)
    csr_tocsc(int n_row, int n_col, int Ap, int Aj, short Ax, int Bp, 
        int Bi, short Bx)
    csr_tocsc(int n_row, int n_col, int Ap, int Aj, int Ax, int Bp, 
        int Bi, int Bx)
    csr_tocsc(int n_row, int n_col, int Ap, int Aj, long long Ax, 
        int Bp, int Bi, long long Bx)
    csr_tocsc(int n_row, int n_col, int Ap, int Aj, float Ax, int Bp, 
        int Bi, float Bx)
    csr_tocsc(int n_row, int n_col, int Ap, int Aj, double Ax, int Bp, 
        int Bi, double Bx)
    csr_tocsc(int n_row, int n_col, int Ap, int Aj, npy_cfloat_wrapper Ax, 
        int Bp, int Bi, npy_cfloat_wrapper Bx)
    csr_tocsc(int n_row, int n_col, int Ap, int Aj, npy_cdouble_wrapper Ax, 
        int Bp, int Bi, npy_cdouble_wrapper Bx)
    """
  return _sparsetools.csr_tocsc(*args)

def csc_tocsr(*args):
  """
    csc_tocsr(int n_row, int n_col, int Ap, int Ai, signed char Ax, 
        int Bp, int Bj, signed char Bx)
    csc_tocsr(int n_row, int n_col, int Ap, int Ai, unsigned char Ax, 
        int Bp, int Bj, unsigned char Bx)
    csc_tocsr(int n_row, int n_col, int Ap, int Ai, short Ax, int Bp, 
        int Bj, short Bx)
    csc_tocsr(int n_row, int n_col, int Ap, int Ai, int Ax, int Bp, 
        int Bj, int Bx)
    csc_tocsr(int n_row, int n_col, int Ap, int Ai, long long Ax, 
        int Bp, int Bj, long long Bx)
    csc_tocsr(int n_row, int n_col, int Ap, int Ai, float Ax, int Bp, 
        int Bj, float Bx)
    csc_tocsr(int n_row, int n_col, int Ap, int Ai, double Ax, int Bp, 
        int Bj, double Bx)
    csc_tocsr(int n_row, int n_col, int Ap, int Ai, npy_cfloat_wrapper Ax, 
        int Bp, int Bj, npy_cfloat_wrapper Bx)
    csc_tocsr(int n_row, int n_col, int Ap, int Ai, npy_cdouble_wrapper Ax, 
        int Bp, int Bj, npy_cdouble_wrapper Bx)
    """
  return _sparsetools.csc_tocsr(*args)

def coo_tocsr(*args):
  """
    coo_tocsr(int n_row, int n_col, int nnz, int Ai, int Aj, signed char Ax, 
        int Bp, int Bj, signed char Bx)
    coo_tocsr(int n_row, int n_col, int nnz, int Ai, int Aj, unsigned char Ax, 
        int Bp, int Bj, unsigned char Bx)
    coo_tocsr(int n_row, int n_col, int nnz, int Ai, int Aj, short Ax, 
        int Bp, int Bj, short Bx)
    coo_tocsr(int n_row, int n_col, int nnz, int Ai, int Aj, int Ax, 
        int Bp, int Bj, int Bx)
    coo_tocsr(int n_row, int n_col, int nnz, int Ai, int Aj, long long Ax, 
        int Bp, int Bj, long long Bx)
    coo_tocsr(int n_row, int n_col, int nnz, int Ai, int Aj, float Ax, 
        int Bp, int Bj, float Bx)
    coo_tocsr(int n_row, int n_col, int nnz, int Ai, int Aj, double Ax, 
        int Bp, int Bj, double Bx)
    coo_tocsr(int n_row, int n_col, int nnz, int Ai, int Aj, npy_cfloat_wrapper Ax, 
        int Bp, int Bj, npy_cfloat_wrapper Bx)
    coo_tocsr(int n_row, int n_col, int nnz, int Ai, int Aj, npy_cdouble_wrapper Ax, 
        int Bp, int Bj, npy_cdouble_wrapper Bx)
    """
  return _sparsetools.coo_tocsr(*args)

def coo_tocsc(*args):
  """
    coo_tocsc(int n_row, int n_col, int nnz, int Ai, int Aj, signed char Ax, 
        int Bp, int Bi, signed char Bx)
    coo_tocsc(int n_row, int n_col, int nnz, int Ai, int Aj, unsigned char Ax, 
        int Bp, int Bi, unsigned char Bx)
    coo_tocsc(int n_row, int n_col, int nnz, int Ai, int Aj, short Ax, 
        int Bp, int Bi, short Bx)
    coo_tocsc(int n_row, int n_col, int nnz, int Ai, int Aj, int Ax, 
        int Bp, int Bi, int Bx)
    coo_tocsc(int n_row, int n_col, int nnz, int Ai, int Aj, long long Ax, 
        int Bp, int Bi, long long Bx)
    coo_tocsc(int n_row, int n_col, int nnz, int Ai, int Aj, float Ax, 
        int Bp, int Bi, float Bx)
    coo_tocsc(int n_row, int n_col, int nnz, int Ai, int Aj, double Ax, 
        int Bp, int Bi, double Bx)
    coo_tocsc(int n_row, int n_col, int nnz, int Ai, int Aj, npy_cfloat_wrapper Ax, 
        int Bp, int Bi, npy_cfloat_wrapper Bx)
    coo_tocsc(int n_row, int n_col, int nnz, int Ai, int Aj, npy_cdouble_wrapper Ax, 
        int Bp, int Bi, npy_cdouble_wrapper Bx)
    """
  return _sparsetools.coo_tocsc(*args)

def csr_matmat_pass2(*args):
  """
    csr_matmat_pass2(int n_row, int n_col, int Ap, int Aj, signed char Ax, 
        int Bp, int Bj, signed char Bx, int Cp, int Cj, 
        signed char Cx)
    csr_matmat_pass2(int n_row, int n_col, int Ap, int Aj, unsigned char Ax, 
        int Bp, int Bj, unsigned char Bx, int Cp, 
        int Cj, unsigned char Cx)
    csr_matmat_pass2(int n_row, int n_col, int Ap, int Aj, short Ax, int Bp, 
        int Bj, short Bx, int Cp, int Cj, short Cx)
    csr_matmat_pass2(int n_row, int n_col, int Ap, int Aj, int Ax, int Bp, 
        int Bj, int Bx, int Cp, int Cj, int Cx)
    csr_matmat_pass2(int n_row, int n_col, int Ap, int Aj, long long Ax, 
        int Bp, int Bj, long long Bx, int Cp, int Cj, 
        long long Cx)
    csr_matmat_pass2(int n_row, int n_col, int Ap, int Aj, float Ax, int Bp, 
        int Bj, float Bx, int Cp, int Cj, float Cx)
    csr_matmat_pass2(int n_row, int n_col, int Ap, int Aj, double Ax, int Bp, 
        int Bj, double Bx, int Cp, int Cj, double Cx)
    csr_matmat_pass2(int n_row, int n_col, int Ap, int Aj, npy_cfloat_wrapper Ax, 
        int Bp, int Bj, npy_cfloat_wrapper Bx, 
        int Cp, int Cj, npy_cfloat_wrapper Cx)
    csr_matmat_pass2(int n_row, int n_col, int Ap, int Aj, npy_cdouble_wrapper Ax, 
        int Bp, int Bj, npy_cdouble_wrapper Bx, 
        int Cp, int Cj, npy_cdouble_wrapper Cx)
    """
  return _sparsetools.csr_matmat_pass2(*args)

def csc_matmat_pass2(*args):
  """
    csc_matmat_pass2(int n_row, int n_col, int Ap, int Ai, signed char Ax, 
        int Bp, int Bi, signed char Bx, int Cp, int Ci, 
        signed char Cx)
    csc_matmat_pass2(int n_row, int n_col, int Ap, int Ai, unsigned char Ax, 
        int Bp, int Bi, unsigned char Bx, int Cp, 
        int Ci, unsigned char Cx)
    csc_matmat_pass2(int n_row, int n_col, int Ap, int Ai, short Ax, int Bp, 
        int Bi, short Bx, int Cp, int Ci, short Cx)
    csc_matmat_pass2(int n_row, int n_col, int Ap, int Ai, int Ax, int Bp, 
        int Bi, int Bx, int Cp, int Ci, int Cx)
    csc_matmat_pass2(int n_row, int n_col, int Ap, int Ai, long long Ax, 
        int Bp, int Bi, long long Bx, int Cp, int Ci, 
        long long Cx)
    csc_matmat_pass2(int n_row, int n_col, int Ap, int Ai, float Ax, int Bp, 
        int Bi, float Bx, int Cp, int Ci, float Cx)
    csc_matmat_pass2(int n_row, int n_col, int Ap, int Ai, double Ax, int Bp, 
        int Bi, double Bx, int Cp, int Ci, double Cx)
    csc_matmat_pass2(int n_row, int n_col, int Ap, int Ai, npy_cfloat_wrapper Ax, 
        int Bp, int Bi, npy_cfloat_wrapper Bx, 
        int Cp, int Ci, npy_cfloat_wrapper Cx)
    csc_matmat_pass2(int n_row, int n_col, int Ap, int Ai, npy_cdouble_wrapper Ax, 
        int Bp, int Bi, npy_cdouble_wrapper Bx, 
        int Cp, int Ci, npy_cdouble_wrapper Cx)
    """
  return _sparsetools.csc_matmat_pass2(*args)

def csr_matvec(*args):
  """
    csr_matvec(int n_row, int n_col, int Ap, int Aj, signed char Ax, 
        signed char Xx, signed char Yx)
    csr_matvec(int n_row, int n_col, int Ap, int Aj, unsigned char Ax, 
        unsigned char Xx, unsigned char Yx)
    csr_matvec(int n_row, int n_col, int Ap, int Aj, short Ax, short Xx, 
        short Yx)
    csr_matvec(int n_row, int n_col, int Ap, int Aj, int Ax, int Xx, 
        int Yx)
    csr_matvec(int n_row, int n_col, int Ap, int Aj, long long Ax, 
        long long Xx, long long Yx)
    csr_matvec(int n_row, int n_col, int Ap, int Aj, float Ax, float Xx, 
        float Yx)
    csr_matvec(int n_row, int n_col, int Ap, int Aj, double Ax, double Xx, 
        double Yx)
    csr_matvec(int n_row, int n_col, int Ap, int Aj, npy_cfloat_wrapper Ax, 
        npy_cfloat_wrapper Xx, npy_cfloat_wrapper Yx)
    csr_matvec(int n_row, int n_col, int Ap, int Aj, npy_cdouble_wrapper Ax, 
        npy_cdouble_wrapper Xx, npy_cdouble_wrapper Yx)
    """
  return _sparsetools.csr_matvec(*args)

def csc_matvec(*args):
  """
    csc_matvec(int n_row, int n_col, int Ap, int Ai, signed char Ax, 
        signed char Xx, signed char Yx)
    csc_matvec(int n_row, int n_col, int Ap, int Ai, unsigned char Ax, 
        unsigned char Xx, unsigned char Yx)
    csc_matvec(int n_row, int n_col, int Ap, int Ai, short Ax, short Xx, 
        short Yx)
    csc_matvec(int n_row, int n_col, int Ap, int Ai, int Ax, int Xx, 
        int Yx)
    csc_matvec(int n_row, int n_col, int Ap, int Ai, long long Ax, 
        long long Xx, long long Yx)
    csc_matvec(int n_row, int n_col, int Ap, int Ai, float Ax, float Xx, 
        float Yx)
    csc_matvec(int n_row, int n_col, int Ap, int Ai, double Ax, double Xx, 
        double Yx)
    csc_matvec(int n_row, int n_col, int Ap, int Ai, npy_cfloat_wrapper Ax, 
        npy_cfloat_wrapper Xx, npy_cfloat_wrapper Yx)
    csc_matvec(int n_row, int n_col, int Ap, int Ai, npy_cdouble_wrapper Ax, 
        npy_cdouble_wrapper Xx, npy_cdouble_wrapper Yx)
    """
  return _sparsetools.csc_matvec(*args)

def bsr_matvec(*args):
  """
    bsr_matvec(int n_brow, int n_bcol, int R, int C, int Ap, int Aj, 
        signed char Ax, signed char Xx, signed char Yx)
    bsr_matvec(int n_brow, int n_bcol, int R, int C, int Ap, int Aj, 
        unsigned char Ax, unsigned char Xx, unsigned char Yx)
    bsr_matvec(int n_brow, int n_bcol, int R, int C, int Ap, int Aj, 
        short Ax, short Xx, short Yx)
    bsr_matvec(int n_brow, int n_bcol, int R, int C, int Ap, int Aj, 
        int Ax, int Xx, int Yx)
    bsr_matvec(int n_brow, int n_bcol, int R, int C, int Ap, int Aj, 
        long long Ax, long long Xx, long long Yx)
    bsr_matvec(int n_brow, int n_bcol, int R, int C, int Ap, int Aj, 
        float Ax, float Xx, float Yx)
    bsr_matvec(int n_brow, int n_bcol, int R, int C, int Ap, int Aj, 
        double Ax, double Xx, double Yx)
    bsr_matvec(int n_brow, int n_bcol, int R, int C, int Ap, int Aj, 
        npy_cfloat_wrapper Ax, npy_cfloat_wrapper Xx, 
        npy_cfloat_wrapper Yx)
    bsr_matvec(int n_brow, int n_bcol, int R, int C, int Ap, int Aj, 
        npy_cdouble_wrapper Ax, npy_cdouble_wrapper Xx, 
        npy_cdouble_wrapper Yx)
    """
  return _sparsetools.bsr_matvec(*args)

def csr_elmul_csr(*args):
  """
    csr_elmul_csr(int n_row, int n_col, int Ap, int Aj, signed char Ax, 
        int Bp, int Bj, signed char Bx, int Cp, int Cj, 
        signed char Cx)
    csr_elmul_csr(int n_row, int n_col, int Ap, int Aj, unsigned char Ax, 
        int Bp, int Bj, unsigned char Bx, int Cp, 
        int Cj, unsigned char Cx)
    csr_elmul_csr(int n_row, int n_col, int Ap, int Aj, short Ax, int Bp, 
        int Bj, short Bx, int Cp, int Cj, short Cx)
    csr_elmul_csr(int n_row, int n_col, int Ap, int Aj, int Ax, int Bp, 
        int Bj, int Bx, int Cp, int Cj, int Cx)
    csr_elmul_csr(int n_row, int n_col, int Ap, int Aj, long long Ax, 
        int Bp, int Bj, long long Bx, int Cp, int Cj, 
        long long Cx)
    csr_elmul_csr(int n_row, int n_col, int Ap, int Aj, float Ax, int Bp, 
        int Bj, float Bx, int Cp, int Cj, float Cx)
    csr_elmul_csr(int n_row, int n_col, int Ap, int Aj, double Ax, int Bp, 
        int Bj, double Bx, int Cp, int Cj, double Cx)
    csr_elmul_csr(int n_row, int n_col, int Ap, int Aj, npy_cfloat_wrapper Ax, 
        int Bp, int Bj, npy_cfloat_wrapper Bx, 
        int Cp, int Cj, npy_cfloat_wrapper Cx)
    csr_elmul_csr(int n_row, int n_col, int Ap, int Aj, npy_cdouble_wrapper Ax, 
        int Bp, int Bj, npy_cdouble_wrapper Bx, 
        int Cp, int Cj, npy_cdouble_wrapper Cx)
    """
  return _sparsetools.csr_elmul_csr(*args)

def csr_eldiv_csr(*args):
  """
    csr_eldiv_csr(int n_row, int n_col, int Ap, int Aj, signed char Ax, 
        int Bp, int Bj, signed char Bx, int Cp, int Cj, 
        signed char Cx)
    csr_eldiv_csr(int n_row, int n_col, int Ap, int Aj, unsigned char Ax, 
        int Bp, int Bj, unsigned char Bx, int Cp, 
        int Cj, unsigned char Cx)
    csr_eldiv_csr(int n_row, int n_col, int Ap, int Aj, short Ax, int Bp, 
        int Bj, short Bx, int Cp, int Cj, short Cx)
    csr_eldiv_csr(int n_row, int n_col, int Ap, int Aj, int Ax, int Bp, 
        int Bj, int Bx, int Cp, int Cj, int Cx)
    csr_eldiv_csr(int n_row, int n_col, int Ap, int Aj, long long Ax, 
        int Bp, int Bj, long long Bx, int Cp, int Cj, 
        long long Cx)
    csr_eldiv_csr(int n_row, int n_col, int Ap, int Aj, float Ax, int Bp, 
        int Bj, float Bx, int Cp, int Cj, float Cx)
    csr_eldiv_csr(int n_row, int n_col, int Ap, int Aj, double Ax, int Bp, 
        int Bj, double Bx, int Cp, int Cj, double Cx)
    csr_eldiv_csr(int n_row, int n_col, int Ap, int Aj, npy_cfloat_wrapper Ax, 
        int Bp, int Bj, npy_cfloat_wrapper Bx, 
        int Cp, int Cj, npy_cfloat_wrapper Cx)
    csr_eldiv_csr(int n_row, int n_col, int Ap, int Aj, npy_cdouble_wrapper Ax, 
        int Bp, int Bj, npy_cdouble_wrapper Bx, 
        int Cp, int Cj, npy_cdouble_wrapper Cx)
    """
  return _sparsetools.csr_eldiv_csr(*args)

def csr_plus_csr(*args):
  """
    csr_plus_csr(int n_row, int n_col, int Ap, int Aj, signed char Ax, 
        int Bp, int Bj, signed char Bx, int Cp, int Cj, 
        signed char Cx)
    csr_plus_csr(int n_row, int n_col, int Ap, int Aj, unsigned char Ax, 
        int Bp, int Bj, unsigned char Bx, int Cp, 
        int Cj, unsigned char Cx)
    csr_plus_csr(int n_row, int n_col, int Ap, int Aj, short Ax, int Bp, 
        int Bj, short Bx, int Cp, int Cj, short Cx)
    csr_plus_csr(int n_row, int n_col, int Ap, int Aj, int Ax, int Bp, 
        int Bj, int Bx, int Cp, int Cj, int Cx)
    csr_plus_csr(int n_row, int n_col, int Ap, int Aj, long long Ax, 
        int Bp, int Bj, long long Bx, int Cp, int Cj, 
        long long Cx)
    csr_plus_csr(int n_row, int n_col, int Ap, int Aj, float Ax, int Bp, 
        int Bj, float Bx, int Cp, int Cj, float Cx)
    csr_plus_csr(int n_row, int n_col, int Ap, int Aj, double Ax, int Bp, 
        int Bj, double Bx, int Cp, int Cj, double Cx)
    csr_plus_csr(int n_row, int n_col, int Ap, int Aj, npy_cfloat_wrapper Ax, 
        int Bp, int Bj, npy_cfloat_wrapper Bx, 
        int Cp, int Cj, npy_cfloat_wrapper Cx)
    csr_plus_csr(int n_row, int n_col, int Ap, int Aj, npy_cdouble_wrapper Ax, 
        int Bp, int Bj, npy_cdouble_wrapper Bx, 
        int Cp, int Cj, npy_cdouble_wrapper Cx)
    """
  return _sparsetools.csr_plus_csr(*args)

def csr_minus_csr(*args):
  """
    csr_minus_csr(int n_row, int n_col, int Ap, int Aj, signed char Ax, 
        int Bp, int Bj, signed char Bx, int Cp, int Cj, 
        signed char Cx)
    csr_minus_csr(int n_row, int n_col, int Ap, int Aj, unsigned char Ax, 
        int Bp, int Bj, unsigned char Bx, int Cp, 
        int Cj, unsigned char Cx)
    csr_minus_csr(int n_row, int n_col, int Ap, int Aj, short Ax, int Bp, 
        int Bj, short Bx, int Cp, int Cj, short Cx)
    csr_minus_csr(int n_row, int n_col, int Ap, int Aj, int Ax, int Bp, 
        int Bj, int Bx, int Cp, int Cj, int Cx)
    csr_minus_csr(int n_row, int n_col, int Ap, int Aj, long long Ax, 
        int Bp, int Bj, long long Bx, int Cp, int Cj, 
        long long Cx)
    csr_minus_csr(int n_row, int n_col, int Ap, int Aj, float Ax, int Bp, 
        int Bj, float Bx, int Cp, int Cj, float Cx)
    csr_minus_csr(int n_row, int n_col, int Ap, int Aj, double Ax, int Bp, 
        int Bj, double Bx, int Cp, int Cj, double Cx)
    csr_minus_csr(int n_row, int n_col, int Ap, int Aj, npy_cfloat_wrapper Ax, 
        int Bp, int Bj, npy_cfloat_wrapper Bx, 
        int Cp, int Cj, npy_cfloat_wrapper Cx)
    csr_minus_csr(int n_row, int n_col, int Ap, int Aj, npy_cdouble_wrapper Ax, 
        int Bp, int Bj, npy_cdouble_wrapper Bx, 
        int Cp, int Cj, npy_cdouble_wrapper Cx)
    """
  return _sparsetools.csr_minus_csr(*args)

def csc_elmul_csc(*args):
  """
    csc_elmul_csc(int n_row, int n_col, int Ap, int Ai, signed char Ax, 
        int Bp, int Bi, signed char Bx, int Cp, int Ci, 
        signed char Cx)
    csc_elmul_csc(int n_row, int n_col, int Ap, int Ai, unsigned char Ax, 
        int Bp, int Bi, unsigned char Bx, int Cp, 
        int Ci, unsigned char Cx)
    csc_elmul_csc(int n_row, int n_col, int Ap, int Ai, short Ax, int Bp, 
        int Bi, short Bx, int Cp, int Ci, short Cx)
    csc_elmul_csc(int n_row, int n_col, int Ap, int Ai, int Ax, int Bp, 
        int Bi, int Bx, int Cp, int Ci, int Cx)
    csc_elmul_csc(int n_row, int n_col, int Ap, int Ai, long long Ax, 
        int Bp, int Bi, long long Bx, int Cp, int Ci, 
        long long Cx)
    csc_elmul_csc(int n_row, int n_col, int Ap, int Ai, float Ax, int Bp, 
        int Bi, float Bx, int Cp, int Ci, float Cx)
    csc_elmul_csc(int n_row, int n_col, int Ap, int Ai, double Ax, int Bp, 
        int Bi, double Bx, int Cp, int Ci, double Cx)
    csc_elmul_csc(int n_row, int n_col, int Ap, int Ai, npy_cfloat_wrapper Ax, 
        int Bp, int Bi, npy_cfloat_wrapper Bx, 
        int Cp, int Ci, npy_cfloat_wrapper Cx)
    csc_elmul_csc(int n_row, int n_col, int Ap, int Ai, npy_cdouble_wrapper Ax, 
        int Bp, int Bi, npy_cdouble_wrapper Bx, 
        int Cp, int Ci, npy_cdouble_wrapper Cx)
    """
  return _sparsetools.csc_elmul_csc(*args)

def csc_eldiv_csc(*args):
  """
    csc_eldiv_csc(int n_row, int n_col, int Ap, int Ai, signed char Ax, 
        int Bp, int Bi, signed char Bx, int Cp, int Ci, 
        signed char Cx)
    csc_eldiv_csc(int n_row, int n_col, int Ap, int Ai, unsigned char Ax, 
        int Bp, int Bi, unsigned char Bx, int Cp, 
        int Ci, unsigned char Cx)
    csc_eldiv_csc(int n_row, int n_col, int Ap, int Ai, short Ax, int Bp, 
        int Bi, short Bx, int Cp, int Ci, short Cx)
    csc_eldiv_csc(int n_row, int n_col, int Ap, int Ai, int Ax, int Bp, 
        int Bi, int Bx, int Cp, int Ci, int Cx)
    csc_eldiv_csc(int n_row, int n_col, int Ap, int Ai, long long Ax, 
        int Bp, int Bi, long long Bx, int Cp, int Ci, 
        long long Cx)
    csc_eldiv_csc(int n_row, int n_col, int Ap, int Ai, float Ax, int Bp, 
        int Bi, float Bx, int Cp, int Ci, float Cx)
    csc_eldiv_csc(int n_row, int n_col, int Ap, int Ai, double Ax, int Bp, 
        int Bi, double Bx, int Cp, int Ci, double Cx)
    csc_eldiv_csc(int n_row, int n_col, int Ap, int Ai, npy_cfloat_wrapper Ax, 
        int Bp, int Bi, npy_cfloat_wrapper Bx, 
        int Cp, int Ci, npy_cfloat_wrapper Cx)
    csc_eldiv_csc(int n_row, int n_col, int Ap, int Ai, npy_cdouble_wrapper Ax, 
        int Bp, int Bi, npy_cdouble_wrapper Bx, 
        int Cp, int Ci, npy_cdouble_wrapper Cx)
    """
  return _sparsetools.csc_eldiv_csc(*args)

def csc_plus_csc(*args):
  """
    csc_plus_csc(int n_row, int n_col, int Ap, int Ai, signed char Ax, 
        int Bp, int Bi, signed char Bx, int Cp, int Ci, 
        signed char Cx)
    csc_plus_csc(int n_row, int n_col, int Ap, int Ai, unsigned char Ax, 
        int Bp, int Bi, unsigned char Bx, int Cp, 
        int Ci, unsigned char Cx)
    csc_plus_csc(int n_row, int n_col, int Ap, int Ai, short Ax, int Bp, 
        int Bi, short Bx, int Cp, int Ci, short Cx)
    csc_plus_csc(int n_row, int n_col, int Ap, int Ai, int Ax, int Bp, 
        int Bi, int Bx, int Cp, int Ci, int Cx)
    csc_plus_csc(int n_row, int n_col, int Ap, int Ai, long long Ax, 
        int Bp, int Bi, long long Bx, int Cp, int Ci, 
        long long Cx)
    csc_plus_csc(int n_row, int n_col, int Ap, int Ai, float Ax, int Bp, 
        int Bi, float Bx, int Cp, int Ci, float Cx)
    csc_plus_csc(int n_row, int n_col, int Ap, int Ai, double Ax, int Bp, 
        int Bi, double Bx, int Cp, int Ci, double Cx)
    csc_plus_csc(int n_row, int n_col, int Ap, int Ai, npy_cfloat_wrapper Ax, 
        int Bp, int Bi, npy_cfloat_wrapper Bx, 
        int Cp, int Ci, npy_cfloat_wrapper Cx)
    csc_plus_csc(int n_row, int n_col, int Ap, int Ai, npy_cdouble_wrapper Ax, 
        int Bp, int Bi, npy_cdouble_wrapper Bx, 
        int Cp, int Ci, npy_cdouble_wrapper Cx)
    """
  return _sparsetools.csc_plus_csc(*args)

def csc_minus_csc(*args):
  """
    csc_minus_csc(int n_row, int n_col, int Ap, int Ai, signed char Ax, 
        int Bp, int Bi, signed char Bx, int Cp, int Ci, 
        signed char Cx)
    csc_minus_csc(int n_row, int n_col, int Ap, int Ai, unsigned char Ax, 
        int Bp, int Bi, unsigned char Bx, int Cp, 
        int Ci, unsigned char Cx)
    csc_minus_csc(int n_row, int n_col, int Ap, int Ai, short Ax, int Bp, 
        int Bi, short Bx, int Cp, int Ci, short Cx)
    csc_minus_csc(int n_row, int n_col, int Ap, int Ai, int Ax, int Bp, 
        int Bi, int Bx, int Cp, int Ci, int Cx)
    csc_minus_csc(int n_row, int n_col, int Ap, int Ai, long long Ax, 
        int Bp, int Bi, long long Bx, int Cp, int Ci, 
        long long Cx)
    csc_minus_csc(int n_row, int n_col, int Ap, int Ai, float Ax, int Bp, 
        int Bi, float Bx, int Cp, int Ci, float Cx)
    csc_minus_csc(int n_row, int n_col, int Ap, int Ai, double Ax, int Bp, 
        int Bi, double Bx, int Cp, int Ci, double Cx)
    csc_minus_csc(int n_row, int n_col, int Ap, int Ai, npy_cfloat_wrapper Ax, 
        int Bp, int Bi, npy_cfloat_wrapper Bx, 
        int Cp, int Ci, npy_cfloat_wrapper Cx)
    csc_minus_csc(int n_row, int n_col, int Ap, int Ai, npy_cdouble_wrapper Ax, 
        int Bp, int Bi, npy_cdouble_wrapper Bx, 
        int Cp, int Ci, npy_cdouble_wrapper Cx)
    """
  return _sparsetools.csc_minus_csc(*args)

def bsr_elmul_bsr(*args):
  """
    bsr_elmul_bsr(int n_row, int n_col, int R, int C, int Ap, int Aj, 
        signed char Ax, int Bp, int Bj, signed char Bx, 
        std::vector<(int)> Cp, std::vector<(int)> Cj, 
        std::vector<(signed char)> Cx)
    bsr_elmul_bsr(int n_row, int n_col, int R, int C, int Ap, int Aj, 
        unsigned char Ax, int Bp, int Bj, unsigned char Bx, 
        std::vector<(int)> Cp, std::vector<(int)> Cj, 
        std::vector<(unsigned char)> Cx)
    bsr_elmul_bsr(int n_row, int n_col, int R, int C, int Ap, int Aj, 
        short Ax, int Bp, int Bj, short Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Cj, std::vector<(short)> Cx)
    bsr_elmul_bsr(int n_row, int n_col, int R, int C, int Ap, int Aj, 
        int Ax, int Bp, int Bj, int Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Cj, std::vector<(int)> Cx)
    bsr_elmul_bsr(int n_row, int n_col, int R, int C, int Ap, int Aj, 
        long long Ax, int Bp, int Bj, long long Bx, 
        std::vector<(int)> Cp, std::vector<(int)> Cj, 
        std::vector<(long long)> Cx)
    bsr_elmul_bsr(int n_row, int n_col, int R, int C, int Ap, int Aj, 
        float Ax, int Bp, int Bj, float Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Cj, std::vector<(float)> Cx)
    bsr_elmul_bsr(int n_row, int n_col, int R, int C, int Ap, int Aj, 
        double Ax, int Bp, int Bj, double Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Cj, std::vector<(double)> Cx)
    bsr_elmul_bsr(int n_row, int n_col, int R, int C, int Ap, int Aj, 
        npy_cfloat_wrapper Ax, int Bp, int Bj, npy_cfloat_wrapper Bx, 
        std::vector<(int)> Cp, std::vector<(int)> Cj, 
        std::vector<(npy_cfloat_wrapper)> Cx)
    bsr_elmul_bsr(int n_row, int n_col, int R, int C, int Ap, int Aj, 
        npy_cdouble_wrapper Ax, int Bp, int Bj, npy_cdouble_wrapper Bx, 
        std::vector<(int)> Cp, std::vector<(int)> Cj, 
        std::vector<(npy_cdouble_wrapper)> Cx)
    """
  return _sparsetools.bsr_elmul_bsr(*args)

def bsr_eldiv_bsr(*args):
  """
    bsr_eldiv_bsr(int n_row, int n_col, int R, int C, int Ap, int Aj, 
        signed char Ax, int Bp, int Bj, signed char Bx, 
        std::vector<(int)> Cp, std::vector<(int)> Cj, 
        std::vector<(signed char)> Cx)
    bsr_eldiv_bsr(int n_row, int n_col, int R, int C, int Ap, int Aj, 
        unsigned char Ax, int Bp, int Bj, unsigned char Bx, 
        std::vector<(int)> Cp, std::vector<(int)> Cj, 
        std::vector<(unsigned char)> Cx)
    bsr_eldiv_bsr(int n_row, int n_col, int R, int C, int Ap, int Aj, 
        short Ax, int Bp, int Bj, short Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Cj, std::vector<(short)> Cx)
    bsr_eldiv_bsr(int n_row, int n_col, int R, int C, int Ap, int Aj, 
        int Ax, int Bp, int Bj, int Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Cj, std::vector<(int)> Cx)
    bsr_eldiv_bsr(int n_row, int n_col, int R, int C, int Ap, int Aj, 
        long long Ax, int Bp, int Bj, long long Bx, 
        std::vector<(int)> Cp, std::vector<(int)> Cj, 
        std::vector<(long long)> Cx)
    bsr_eldiv_bsr(int n_row, int n_col, int R, int C, int Ap, int Aj, 
        float Ax, int Bp, int Bj, float Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Cj, std::vector<(float)> Cx)
    bsr_eldiv_bsr(int n_row, int n_col, int R, int C, int Ap, int Aj, 
        double Ax, int Bp, int Bj, double Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Cj, std::vector<(double)> Cx)
    bsr_eldiv_bsr(int n_row, int n_col, int R, int C, int Ap, int Aj, 
        npy_cfloat_wrapper Ax, int Bp, int Bj, npy_cfloat_wrapper Bx, 
        std::vector<(int)> Cp, std::vector<(int)> Cj, 
        std::vector<(npy_cfloat_wrapper)> Cx)
    bsr_eldiv_bsr(int n_row, int n_col, int R, int C, int Ap, int Aj, 
        npy_cdouble_wrapper Ax, int Bp, int Bj, npy_cdouble_wrapper Bx, 
        std::vector<(int)> Cp, std::vector<(int)> Cj, 
        std::vector<(npy_cdouble_wrapper)> Cx)
    """
  return _sparsetools.bsr_eldiv_bsr(*args)

def bsr_plus_bsr(*args):
  """
    bsr_plus_bsr(int n_row, int n_col, int R, int C, int Ap, int Aj, 
        signed char Ax, int Bp, int Bj, signed char Bx, 
        std::vector<(int)> Cp, std::vector<(int)> Cj, 
        std::vector<(signed char)> Cx)
    bsr_plus_bsr(int n_row, int n_col, int R, int C, int Ap, int Aj, 
        unsigned char Ax, int Bp, int Bj, unsigned char Bx, 
        std::vector<(int)> Cp, std::vector<(int)> Cj, 
        std::vector<(unsigned char)> Cx)
    bsr_plus_bsr(int n_row, int n_col, int R, int C, int Ap, int Aj, 
        short Ax, int Bp, int Bj, short Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Cj, std::vector<(short)> Cx)
    bsr_plus_bsr(int n_row, int n_col, int R, int C, int Ap, int Aj, 
        int Ax, int Bp, int Bj, int Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Cj, std::vector<(int)> Cx)
    bsr_plus_bsr(int n_row, int n_col, int R, int C, int Ap, int Aj, 
        long long Ax, int Bp, int Bj, long long Bx, 
        std::vector<(int)> Cp, std::vector<(int)> Cj, 
        std::vector<(long long)> Cx)
    bsr_plus_bsr(int n_row, int n_col, int R, int C, int Ap, int Aj, 
        float Ax, int Bp, int Bj, float Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Cj, std::vector<(float)> Cx)
    bsr_plus_bsr(int n_row, int n_col, int R, int C, int Ap, int Aj, 
        double Ax, int Bp, int Bj, double Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Cj, std::vector<(double)> Cx)
    bsr_plus_bsr(int n_row, int n_col, int R, int C, int Ap, int Aj, 
        npy_cfloat_wrapper Ax, int Bp, int Bj, npy_cfloat_wrapper Bx, 
        std::vector<(int)> Cp, std::vector<(int)> Cj, 
        std::vector<(npy_cfloat_wrapper)> Cx)
    bsr_plus_bsr(int n_row, int n_col, int R, int C, int Ap, int Aj, 
        npy_cdouble_wrapper Ax, int Bp, int Bj, npy_cdouble_wrapper Bx, 
        std::vector<(int)> Cp, std::vector<(int)> Cj, 
        std::vector<(npy_cdouble_wrapper)> Cx)
    """
  return _sparsetools.bsr_plus_bsr(*args)

def bsr_minus_bsr(*args):
  """
    bsr_minus_bsr(int n_row, int n_col, int R, int C, int Ap, int Aj, 
        signed char Ax, int Bp, int Bj, signed char Bx, 
        std::vector<(int)> Cp, std::vector<(int)> Cj, 
        std::vector<(signed char)> Cx)
    bsr_minus_bsr(int n_row, int n_col, int R, int C, int Ap, int Aj, 
        unsigned char Ax, int Bp, int Bj, unsigned char Bx, 
        std::vector<(int)> Cp, std::vector<(int)> Cj, 
        std::vector<(unsigned char)> Cx)
    bsr_minus_bsr(int n_row, int n_col, int R, int C, int Ap, int Aj, 
        short Ax, int Bp, int Bj, short Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Cj, std::vector<(short)> Cx)
    bsr_minus_bsr(int n_row, int n_col, int R, int C, int Ap, int Aj, 
        int Ax, int Bp, int Bj, int Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Cj, std::vector<(int)> Cx)
    bsr_minus_bsr(int n_row, int n_col, int R, int C, int Ap, int Aj, 
        long long Ax, int Bp, int Bj, long long Bx, 
        std::vector<(int)> Cp, std::vector<(int)> Cj, 
        std::vector<(long long)> Cx)
    bsr_minus_bsr(int n_row, int n_col, int R, int C, int Ap, int Aj, 
        float Ax, int Bp, int Bj, float Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Cj, std::vector<(float)> Cx)
    bsr_minus_bsr(int n_row, int n_col, int R, int C, int Ap, int Aj, 
        double Ax, int Bp, int Bj, double Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Cj, std::vector<(double)> Cx)
    bsr_minus_bsr(int n_row, int n_col, int R, int C, int Ap, int Aj, 
        npy_cfloat_wrapper Ax, int Bp, int Bj, npy_cfloat_wrapper Bx, 
        std::vector<(int)> Cp, std::vector<(int)> Cj, 
        std::vector<(npy_cfloat_wrapper)> Cx)
    bsr_minus_bsr(int n_row, int n_col, int R, int C, int Ap, int Aj, 
        npy_cdouble_wrapper Ax, int Bp, int Bj, npy_cdouble_wrapper Bx, 
        std::vector<(int)> Cp, std::vector<(int)> Cj, 
        std::vector<(npy_cdouble_wrapper)> Cx)
    """
  return _sparsetools.bsr_minus_bsr(*args)

def csr_sort_indices(*args):
  """
    csr_sort_indices(int n_row, int Ap, int Aj, signed char Ax)
    csr_sort_indices(int n_row, int Ap, int Aj, unsigned char Ax)
    csr_sort_indices(int n_row, int Ap, int Aj, short Ax)
    csr_sort_indices(int n_row, int Ap, int Aj, int Ax)
    csr_sort_indices(int n_row, int Ap, int Aj, long long Ax)
    csr_sort_indices(int n_row, int Ap, int Aj, float Ax)
    csr_sort_indices(int n_row, int Ap, int Aj, double Ax)
    csr_sort_indices(int n_row, int Ap, int Aj, npy_cfloat_wrapper Ax)
    csr_sort_indices(int n_row, int Ap, int Aj, npy_cdouble_wrapper Ax)
    """
  return _sparsetools.csr_sort_indices(*args)

def csr_sum_duplicates(*args):
  """
    csr_sum_duplicates(int n_row, int n_col, int Ap, int Aj, signed char Ax)
    csr_sum_duplicates(int n_row, int n_col, int Ap, int Aj, unsigned char Ax)
    csr_sum_duplicates(int n_row, int n_col, int Ap, int Aj, short Ax)
    csr_sum_duplicates(int n_row, int n_col, int Ap, int Aj, int Ax)
    csr_sum_duplicates(int n_row, int n_col, int Ap, int Aj, long long Ax)
    csr_sum_duplicates(int n_row, int n_col, int Ap, int Aj, float Ax)
    csr_sum_duplicates(int n_row, int n_col, int Ap, int Aj, double Ax)
    csr_sum_duplicates(int n_row, int n_col, int Ap, int Aj, npy_cfloat_wrapper Ax)
    csr_sum_duplicates(int n_row, int n_col, int Ap, int Aj, npy_cdouble_wrapper Ax)
    """
  return _sparsetools.csr_sum_duplicates(*args)

def get_csr_submatrix(*args):
  """
    get_csr_submatrix(int n_row, int n_col, int Ap, int Aj, signed char Ax, 
        int ir0, int ir1, int ic0, int ic1, std::vector<(int)> Bp, 
        std::vector<(int)> Bj, std::vector<(signed char)> Bx)
    get_csr_submatrix(int n_row, int n_col, int Ap, int Aj, unsigned char Ax, 
        int ir0, int ir1, int ic0, int ic1, std::vector<(int)> Bp, 
        std::vector<(int)> Bj, std::vector<(unsigned char)> Bx)
    get_csr_submatrix(int n_row, int n_col, int Ap, int Aj, short Ax, int ir0, 
        int ir1, int ic0, int ic1, std::vector<(int)> Bp, 
        std::vector<(int)> Bj, std::vector<(short)> Bx)
    get_csr_submatrix(int n_row, int n_col, int Ap, int Aj, int Ax, int ir0, 
        int ir1, int ic0, int ic1, std::vector<(int)> Bp, 
        std::vector<(int)> Bj, std::vector<(int)> Bx)
    get_csr_submatrix(int n_row, int n_col, int Ap, int Aj, long long Ax, 
        int ir0, int ir1, int ic0, int ic1, std::vector<(int)> Bp, 
        std::vector<(int)> Bj, std::vector<(long long)> Bx)
    get_csr_submatrix(int n_row, int n_col, int Ap, int Aj, float Ax, int ir0, 
        int ir1, int ic0, int ic1, std::vector<(int)> Bp, 
        std::vector<(int)> Bj, std::vector<(float)> Bx)
    get_csr_submatrix(int n_row, int n_col, int Ap, int Aj, double Ax, int ir0, 
        int ir1, int ic0, int ic1, std::vector<(int)> Bp, 
        std::vector<(int)> Bj, std::vector<(double)> Bx)
    get_csr_submatrix(int n_row, int n_col, int Ap, int Aj, npy_cfloat_wrapper Ax, 
        int ir0, int ir1, int ic0, int ic1, 
        std::vector<(int)> Bp, std::vector<(int)> Bj, 
        std::vector<(npy_cfloat_wrapper)> Bx)
    get_csr_submatrix(int n_row, int n_col, int Ap, int Aj, npy_cdouble_wrapper Ax, 
        int ir0, int ir1, int ic0, int ic1, 
        std::vector<(int)> Bp, std::vector<(int)> Bj, 
        std::vector<(npy_cdouble_wrapper)> Bx)
    """
  return _sparsetools.get_csr_submatrix(*args)


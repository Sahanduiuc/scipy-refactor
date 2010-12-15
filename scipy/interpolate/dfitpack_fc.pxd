from fwrap_ktp cimport *

cdef extern from "dfitpack_fc.h":
    void bispeu "F_FUNC(bispeu,BISPEU)"(
        fwr_real_x8_t * tx,
        fwi_integer_t * nx,
        fwr_real_x8_t * ty,
        fwi_integer_t * ny,
        fwr_real_x8_t * c,
        fwi_integer_t * kx,
        fwi_integer_t * ky,
        fwr_real_x8_t * x,
        fwr_real_x8_t * y,
        fwr_real_x8_t * z,
        fwi_integer_t * m,
        fwr_real_x8_t * wrk,
        fwi_integer_t * lwrk,
        fwi_integer_t * ier
    )
    void bispev "F_FUNC(bispev,BISPEV)"(
        fwr_real_x8_t * tx,
        fwi_integer_t * nx,
        fwr_real_x8_t * ty,
        fwi_integer_t * ny,
        fwr_real_x8_t * c,
        fwi_integer_t * kx,
        fwi_integer_t * ky,
        fwr_real_x8_t * x,
        fwi_integer_t * mx,
        fwr_real_x8_t * y,
        fwi_integer_t * my,
        fwr_real_x8_t * z,
        fwr_real_x8_t * wrk,
        fwi_integer_t * lwrk,
        fwi_integer_t * iwrk,
        fwi_integer_t * kwrk,
        fwi_integer_t * ier
    )
    void curfit "F_FUNC(curfit,CURFIT)"(
        fwi_integer_t * iopt,
        fwi_integer_t * m,
        fwr_real_x8_t * x,
        fwr_real_x8_t * y,
        fwr_real_x8_t * w,
        fwr_real_x8_t * xb,
        fwr_real_x8_t * xe,
        fwi_integer_t * k,
        fwr_real_x8_t * s,
        fwi_integer_t * nest,
        fwi_integer_t * n,
        fwr_real_x8_t * t,
        fwr_real_x8_t * c,
        fwr_real_x8_t * fp,
        fwr_real_x8_t * wrk,
        fwi_integer_t * lwrk,
        fwi_integer_t * iwrk,
        fwi_integer_t * ier
    )
    fwr_real_x8_t dblint "F_FUNC(dblint,DBLINT)"(
        fwr_real_x8_t * tx,
        fwi_integer_t * nx,
        fwr_real_x8_t * ty,
        fwi_integer_t * ny,
        fwr_real_x8_t * c,
        fwi_integer_t * kx,
        fwi_integer_t * ky,
        fwr_real_x8_t * xb,
        fwr_real_x8_t * xe,
        fwr_real_x8_t * yb,
        fwr_real_x8_t * ye,
        fwr_real_x8_t * wrk
    )
    void fpcurf "F_FUNC(fpcurf,FPCURF)"(
        fwi_integer_t * iopt,
        fwr_real_x8_t * x,
        fwr_real_x8_t * y,
        fwr_real_x8_t * w,
        fwi_integer_t * m,
        fwr_real_x8_t * xb,
        fwr_real_x8_t * xe,
        fwi_integer_t * k,
        fwr_real_x8_t * s,
        fwi_integer_t * nest,
        fwr_real_x8_t * tol,
        fwi_integer_t * maxit,
        fwi_integer_t * k1,
        fwi_integer_t * k2,
        fwi_integer_t * n,
        fwr_real_x8_t * t,
        fwr_real_x8_t * c,
        fwr_real_x8_t * fp,
        fwr_real_x8_t * fpint,
        fwr_real_x8_t * z,
        fwr_real_x8_t * a,
        fwr_real_x8_t * b,
        fwr_real_x8_t * g,
        fwr_real_x8_t * q,
        fwi_integer_t * nrdata,
        fwi_integer_t * ier
    )
    void percur "F_FUNC(percur,PERCUR)"(
        fwi_integer_t * iopt,
        fwi_integer_t * m,
        fwr_real_x8_t * x,
        fwr_real_x8_t * y,
        fwr_real_x8_t * w,
        fwi_integer_t * k,
        fwr_real_x8_t * s,
        fwi_integer_t * nest,
        fwi_integer_t * n,
        fwr_real_x8_t * t,
        fwr_real_x8_t * c,
        fwr_real_x8_t * fp,
        fwr_real_x8_t * wrk,
        fwi_integer_t * lwrk,
        fwi_integer_t * iwrk,
        fwi_integer_t * ier
    )
    void regrid "F_FUNC(regrid,REGRID)"(
        fwi_integer_t * iopt,
        fwi_integer_t * mx,
        fwr_real_x8_t * x,
        fwi_integer_t * my,
        fwr_real_x8_t * y,
        fwr_real_x8_t * z,
        fwr_real_x8_t * xb,
        fwr_real_x8_t * xe,
        fwr_real_x8_t * yb,
        fwr_real_x8_t * ye,
        fwi_integer_t * kx,
        fwi_integer_t * ky,
        fwr_real_x8_t * s,
        fwi_integer_t * nxest,
        fwi_integer_t * nyest,
        fwi_integer_t * nx,
        fwr_real_x8_t * tx,
        fwi_integer_t * ny,
        fwr_real_x8_t * ty,
        fwr_real_x8_t * c,
        fwr_real_x8_t * fp,
        fwr_real_x8_t * wrk,
        fwi_integer_t * lwrk,
        fwi_integer_t * iwrk,
        fwi_integer_t * kwrk,
        fwi_integer_t * ier
    )
    void spalde "F_FUNC(spalde,SPALDE)"(
        fwr_real_x8_t * t,
        fwi_integer_t * n,
        fwr_real_x8_t * c,
        fwi_integer_t * k1,
        fwr_real_x8_t * x,
        fwr_real_x8_t * d,
        fwi_integer_t * ier
    )
    void splder "F_FUNC(splder,SPLDER)"(
        fwr_real_x8_t * t,
        fwi_integer_t * n,
        fwr_real_x8_t * c,
        fwi_integer_t * k,
        fwi_integer_t * nu,
        fwr_real_x8_t * x,
        fwr_real_x8_t * y,
        fwi_integer_t * m,
        fwi_integer_t * e,
        fwr_real_x8_t * wrk,
        fwi_integer_t * ier
    )
    void splev "F_FUNC(splev,SPLEV)"(
        fwr_real_x8_t * t,
        fwi_integer_t * n,
        fwr_real_x8_t * c,
        fwi_integer_t * k,
        fwr_real_x8_t * x,
        fwr_real_x8_t * y,
        fwi_integer_t * m,
        fwi_integer_t * e,
        fwi_integer_t * ier
    )
    fwr_real_x8_t splint "F_FUNC(splint,SPLINT)"(
        fwr_real_x8_t * t,
        fwi_integer_t * n,
        fwr_real_x8_t * c,
        fwi_integer_t * k,
        fwr_real_x8_t * a,
        fwr_real_x8_t * b,
        fwr_real_x8_t * wrk
    )
    void sproot "F_FUNC(sproot,SPROOT)"(
        fwr_real_x8_t * t,
        fwi_integer_t * n,
        fwr_real_x8_t * c,
        fwr_real_x8_t * zero,
        fwi_integer_t * mest,
        fwi_integer_t * m,
        fwi_integer_t * ier
    )
    void surfit "F_FUNC(surfit,SURFIT)"(
        fwi_integer_t * iopt,
        fwi_integer_t * m,
        fwr_real_x8_t * x,
        fwr_real_x8_t * y,
        fwr_real_x8_t * z,
        fwr_real_x8_t * w,
        fwr_real_x8_t * xb,
        fwr_real_x8_t * xe,
        fwr_real_x8_t * yb,
        fwr_real_x8_t * ye,
        fwi_integer_t * kx,
        fwi_integer_t * ky,
        fwr_real_x8_t * s,
        fwi_integer_t * nxest,
        fwi_integer_t * nyest,
        fwi_integer_t * nmax,
        fwr_real_x8_t * eps,
        fwi_integer_t * nx,
        fwr_real_x8_t * tx,
        fwi_integer_t * ny,
        fwr_real_x8_t * ty,
        fwr_real_x8_t * c,
        fwr_real_x8_t * fp,
        fwr_real_x8_t * wrk1,
        fwi_integer_t * lwrk1,
        fwr_real_x8_t * wrk2,
        fwi_integer_t * lwrk2,
        fwi_integer_t * iwrk,
        fwi_integer_t * kwrk,
        fwi_integer_t * ier
    )
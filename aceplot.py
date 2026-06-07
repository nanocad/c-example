# Copyright (C) 2021 J. K. Dewhurst, S. Sharma and E. K. U. Gross.
# This file is distributed under the terms of the GNU General Public License.
# See the file COPYING for license details.

def aceplot():
    """
    Plot the fermionic and bosonic anomalous correlation entropy.
    
    This function assumes that the following modules exist and provide
    the necessary variables and functions:
    - modmain
    - modphonon
    - modbog
    """
    # Import required modules (these need to be defined elsewhere)
    from modmain import init0, init1, init2, ngridk, ivkiknr, ivkik, vkc, occmax
    from modphonon import initeph, ngridq, ivqiqnr, ivqiq, vqc
    from modbog import nstsv, vnorm, nbph, xnorm
    
    import numpy as np
    
    # Initialise universal variables
    init0()
    init1()
    init2()
    initeph()
    
    # ----------------------------------------------------------
    #     plot the fermionic anomalous correlation entropy
    # ----------------------------------------------------------
    with open('FACE3D.OUT', 'w') as f:
        # Write grid size header
        f.write(f"{ngridk[0]:6d}{ngridk[1]:6d}{ngridk[2]:6d} : grid size\n")
        
        for i3 in range(ngridk[2]):
            for i2 in range(ngridk[1]):
                for i1 in range(ngridk[0]):
                    ik = ivkiknr[i1, i2, i3]
                    jk = ivkik[i1, i2, i3]
                    
                    ace = 0.0
                    for ist in range(1, nstsv + 1):
                        vn = vnorm(ist, jk)
                        if (vn > 0.0) and (vn < 1.0):
                            ace += vn * np.log(vn) + (1.0 - vn) * np.log(1.0 - vn)
                    
                    ace = -occmax * ace
                    f.write(f"{vkc[0, ik]:18.10e}{vkc[1, ik]:18.10e}{vkc[2, ik]:18.10e}{ace:18.10e}\n")
    
    # --------------------------------------------------------
    #     plot the bosonic anomalous correlation entropy
    # --------------------------------------------------------
    with open('BACE3D.OUT', 'w') as f:
        # Write grid size header
        f.write(f"{ngridq[0]:6d}{ngridq[1]:6d}{ngridq[2]:6d} : grid size\n")
        
        for i3 in range(ngridq[2]):
            for i2 in range(ngridq[1]):
                for i1 in range(ngridq[0]):
                    iq = ivqiqnr[i1, i2, i3]
                    jq = ivqiq[i1, i2, i3]
                    
                    ace = 0.0
                    for i in range(1, nbph + 1):
                        xn = xnorm(i, jq)
                        if xn > 0.0:
                            ace += xn * np.log(xn) - (1.0 + xn) * np.log(1.0 + xn)
                    
                    ace = -ace
                    f.write(f"{vqc[0, iq]:18.10e}{vqc[1, iq]:18.10e}{vqc[2, iq]:18.10e}{ace:18.10e}\n")
    
    print()
    print("Info(aceplot):")
    print(" 3D fermionic anomalous correlation entropy written to FACE3D.OUT")
    print(" 3D bosonic anomalous correlation entropy written to BACE3D.OUT")


if __name__ == "__main__":
    aceplot()

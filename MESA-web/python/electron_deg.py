import numpy as np
from MESAreader import get_src_col, boltzm
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


if __name__ == "__main__":
    root = "../1Msun_4e9yr/"
    pfile = root+'profile8.data'
    src, col = get_src_col(pfile)
    m = src[:, col.index("mass")]
    eta = src[:, col.index("eta")]
    P = src[:, col.index("pressure")]
    rho = 10.0**(src[:, col.index("logRho")])
    mu = src[:, col.index("mu")]
    T = 10.0**(src[:, col.index("logT")])
    m_u = 1.66e-24 # atomic mass unit
    fig = plt.figure()
    gs = gridspec.GridSpec(150, 100)
    ax = fig.add_subplot(gs[:, :])
    bx = ax.twinx()
    ax.plot(m, np.log10(P), label=r"$P_{\rm tot}$")
    ax.plot(m, np.log10((rho/(mu*m_u))*boltzm*T), label=r"$P_{\rm ideal\ gas}$")
    bx.plot(m, eta, ls='--', c='r')
    bx.set_ylabel(r"$\eta$", c="r")
    ax.set_xlabel(r"$m \ [M_\odot]$")
    ax.set_ylabel(r"$\log_{10}(P/\mathrm{[dyne\ cm^{-2}]})$")
    ax.legend()
    plt.show()

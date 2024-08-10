from MESAreader import get_src_col, read_MESA_header
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


def P_polytropic(rho, K=1e17/(100)**(5/3), gamma=5/3):
    """ N.B.: to chose the polytropic constant K I cheated by looking at the inner value of P and rho"""
    return K*rho**gamma


if __name__== "__main__":
    root="../0.3Msun_1e8yr/"
    pfile = root+"profile111.data"
    src, col = get_src_col(pfile)
    src_header, col_header = read_MESA_header(pfile)
    rho = 10.0**(src[:, col.index("logRho")])
    P = src[:, col.index("pressure")]
    # T = 10.0**(src[:, col.index("logT")])
    fig = plt.figure()
    gs = gridspec.GridSpec(150, 100)
    ax = fig.add_subplot(gs[:, :])
    # bx = ax.twinx()
    ax.set_title("mass: " +
                 f"{src[0, col.index('mass')]:.1f}"+r"$M_\odot$ " +
                 "age: " +
                 f"{float(src_header[col_header.index('star_age')])*1e-6:.0f}" +
                 r"Myr", fontsize=30)
    ax.loglog(rho, P, label=r"MESA-web")
    # bx.loglog(rho, T, c='r')
    # add polytropic EOS
    ax.plot(rho, P_polytropic(rho), ls='--', label=r"Polytrope $\Gamma=5/3$")
    # ax.invert_xaxis()
    ax.legend()
    ax.set_ylabel(r"Pressure [$\mathrm{dyne\ cm^{-2}}$]")
    # bx.set_ylabel(r"Temperature [$\mathrm{K}$]", color='red')
    ax.set_xlabel(r"Density [$\mathrm{g\ cm^{-3}}$]")
    plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Access the default color cycle
default_colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
c1 = default_colors[0]
c2 = default_colors[1]
c3 = default_colors[2]

# plt.rcParams["text.usetex"] = True

"""
Plots for Question 4
"""


def plot_ln_k_solow(k_time, time, title=None):
    fig, ax = plt.subplots()
    ax.plot(
        time,
        np.log(k_time[:, 1]),
        label=r"$\Delta g_L=0.005$",
        linewidth=3,
        color="blue",
    )
    ax.plot(
        time, np.log(k_time[:, 2]), label=r"$\Delta g_L=0.02$", linewidth=3, color="red"
    )
    ax.plot(
        time,
        np.log(k_time[:, 0]),
        label=r"No change in $g_L$",
        linewidth=3,
        color="black",
    )
    ax.set_xlabel("time", fontsize=14)
    ax.set_ylabel("k", fontsize=14)
    ax.legend(prop={"size": 12})

    ax.set_xlim(0, time[-1])
    ax.set_ylim(
        np.min(np.log(k_time[:, 2])) - 0.015, np.max(np.log(k_time[:, 2])) + 0.015
    )

    if title is not None:
        ax.set_title(title, fontsize=16)

    # save to pdf
    return fig, ax


def plot_ln_k_exo_TFP(k_time, time, title="Time path of capital per worker"):
    return plot_ln_k_solow(k_time, time, title=title)


def plot_ln_k_A_endo_TFP(k_time, time, title=None, savepath=None, Tb=10_000):
    fig, ax = plt.subplots()
    ax.plot(
        time[:Tb],
        np.log(k_time[:Tb, 1]),
        label=r"$\Delta$ $g_L=0.005$",
        linewidth=3,
        color="blue",
    )
    ax.plot(
        time[:Tb],
        np.log(k_time[:Tb, 2]),
        label=r"$\Delta$ $g_L=0.02$",
        linewidth=3,
        color="red",
    )
    ax.plot(
        time[:Tb],
        np.log(k_time[:Tb, 0]),
        label=r"No change in $g_L$",
        linewidth=3,
        color="black",
    )

    ax.set_xlim(0, 100)
    ax.set_ylim(
        np.min(np.log(k_time[:Tb, 2])) - 0.015, np.max(np.log(k_time[:Tb, 2])) + 0.022
    )

    ax.set_xlabel("time", fontsize=14)
    ax.set_ylabel(r"$\ln(k)$", fontsize=14)
    ax.legend(prop={"size": 12})
    if title is not None:
        ax.set_title(title, fontsize=16)

    return fig, ax


def plot_g_A_endo_TFP(g_A, time, title=None, savepath=None):
    fig, ax = plt.subplots()
    ax.plot(time, g_A[:, 1], label=r"$\Delta$ $g_L=0.005$", linewidth=3, color="blue")
    ax.plot(time, g_A[:, 2], label=r"$\Delta$ $g_L=0.02$", linewidth=3, color="red")
    ax.plot(time, g_A[:, 0], label=r"No change in $g_L$", linewidth=3, color="black")

    ax.set_xlim(0, time[-1])
    ax.set_ylim(0, 0.035)

    ax.set_xlabel("time", fontsize=14)
    ax.set_ylabel(r"$g_A$", fontsize=14)
    ax.set_ylabel(r"$g_A$", fontsize=14)
    ax.legend(prop={"size": 12})

    return fig, ax


def plot_log_L_A(L_A, A, time, title=None):
    fig, ax = plt.subplots()
    ax.plot(time, np.log(L_A[:, 1]), linewidth=3, color="blue")
    ax.plot(time, np.log(A[:, 1]), linestyle=":", linewidth=3, color="blue")
    ax.plot(time, np.log(L_A[:, 2]), linewidth=3, color="red", label=r"$\ln(L_A)$")
    ax.plot(time, np.log(A[:, 2]), linestyle=":", linewidth=3, color="red")
    ax.plot(time, np.log(L_A[:, 0]), linewidth=3, color="black")
    ax.plot(time, np.log(A[:, 0]), linestyle=":", linewidth=3, color="black")

    ax.legend(prop={"size": 12})
    ax.set_xlabel("time", fontsize=14)
    ax.set_ylabel(r"$\ln(L_A)$ and $\ln(A)$", fontsize=14)
    if title is not None:
        ax.set_title(title, fontsize=16)

    return fig, ax


def plot_g_L_endo_TFP(g_L, time, title=None, savepath=None):
    nulls = np.zeros(len(time))

    fig, ax = plt.subplots()
    ax.plot(
        time[1_000:],
        nulls[1_000:] + g_L[1],
        label=r"$\Delta g_L=0.005$",
        linewidth=3,
        color="blue",
    )
    ax.plot(
        time[1_000:],
        nulls[1_000:] + g_L[2],
        label=r"$\Delta g_L=0.02$",
        linewidth=3,
        color="red",
    )
    ax.plot(
        time, nulls + g_L[0], label=r"No change in $g_L$", linewidth=3, color="black"
    )

    ax.set_xlim(0, time[-1])
    ax.set_ylim(0, 0.035)

    ax.set_xlabel("time", fontsize=14)
    ax.set_ylabel(r"$g_L$", fontsize=14)
    ax.set_ylabel(r"$g_L$", fontsize=14)
    ax.legend(prop={"size": 12})
    if title is not None:
        ax.set_title(title, fontsize=16)

    return fig, ax

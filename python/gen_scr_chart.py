import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

T = np.linspace(100, 700, 600)

# Low-Temp SCR (Mn/V-based): bell curve, peak ~220°C, max ~92%
def low_temp_scr(T):
    peak, sigma, h = 220, 45, 92
    return h * np.exp(-((T - peak)**2) / (2 * sigma**2))

# High-Temp SCR (V2O5-WO3): bell curve, peak ~390°C, max ~95%
def high_temp_scr(T):
    peak, sigma, h = 390, 85, 95
    return h * np.exp(-((T - peak)**2) / (2 * sigma**2))

# Urea-to-NH3 Conversion: sigmoid, 50% at ~220°C, 100% by ~310°C
def urea_conversion(T):
    return 100 / (1 + np.exp(-0.055 * (T - 240)))

# NH3 Slip Potential: high at low temp, trough in middle, rises at high temp
def nh3_slip(T):
    low_part = 50 * np.exp(-((T - 100)**2) / (2 * 50**2))
    high_part = 40 * np.exp(-((T - 700)**2) / (2 * 100**2))
    # trough around 300-400
    return np.clip(low_part + high_part, 0, 100)

fig, ax1 = plt.subplots(figsize=(11, 6))

# Shaded regions
ax1.axvspan(150, 300, alpha=0.18, color='steelblue', label='Low-Temp Ops Range')
ax1.axvspan(320, 480, alpha=0.18, color='salmon', label='High-Temp Ops Range')

# Primary axis: NOx efficiency
ax1.plot(T, low_temp_scr(T), color='steelblue', linewidth=2.5,
         label='Realistic Low-Temp SCR (Mn/V-based)')
ax1.plot(T, high_temp_scr(T), color='firebrick', linewidth=2.5,
         label='Realistic High-Temp SCR (V2O5-WO3)')
ax1.set_xlabel('Temperature (°C)', fontsize=12)
ax1.set_ylabel('NO$_x$ Removal Efficiency (%)', fontsize=12)
ax1.set_xlim(100, 700)
ax1.set_ylim(0, 105)
ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f'{int(v)}'))

# Secondary axis: Conversion / Slip Rate
ax2 = ax1.twinx()
ax2.plot(T, urea_conversion(T), color='orange', linewidth=2, linestyle='--',
         label='Urea-to-NH3 Conversion')
ax2.plot(T, nh3_slip(T), color='green', linewidth=1.8, linestyle=':',
         label='NH3 Slip Potential')
ax2.set_ylabel('Conversion / Slip Rate (%)', fontsize=12)
ax2.set_ylim(0, 105)

# Combined legend
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper right', fontsize=9,
           framealpha=0.9)

ax1.set_title('Realistic SCR Performance & Urea Chemistry Analysis', fontsize=13, pad=10)
ax1.grid(True, linestyle='--', alpha=0.4)

plt.tight_layout()
out = r'c:\Users\mosuk\문서_기존\Git\My_home\img\scr_performance.png'
plt.savefig(out, dpi=150, bbox_inches='tight')
print('Saved:', out)

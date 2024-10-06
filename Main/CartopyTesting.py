import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt

ax = plt.axes(projection=ccrs.PlateCarree())

ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS)

plt.show()
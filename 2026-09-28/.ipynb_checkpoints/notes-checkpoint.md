# 2026-09-28

## Chu de hom nay
Matplotlib

## Nhung gi da hoc
- Thư viện matplotlib và colifornia cities

## Code / vi du
```
population, area = cities['population_total'], cities['area_total_km2']
plt.scatter(long, lat, c = np.log10(population), cmap = "viridis", s = area);
plt.xlabel("longtitude");
plt.ylabel("latitude");
plt.colorbar(label = 'log$_(10)$(population)');
area_range = [50, 100, 200, 500]
for i in area_range:
    plt.scatter([], [], s = i, label = str(i) + 'km^2', c = 'k', alpha = 0.5);
plt.legend(labelspacing = 1, title = 'area_sizes');

```

## Cau hoi con thac mac
- 

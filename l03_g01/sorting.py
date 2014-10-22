#!/usr/bin/python3
# Koeckman, Andi

a="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean varius eu sem eget luctus. In sagittis semper euismod. Pellentesque in nibh vel dolor pulvinar malesuada. Proin ut nisl augue. Duis a urna augue. Praesent euismod turpis sed convallis accumsan. Sed ac pretium ante. Mauris fringilla vitae nibh hendrerit feugiat."
b=a.split() #neue variable b mit gespliteten paramaetern von a
b.sort(reverse=True,key=str.lower) #sortiert help(sort)
print("Diese List ist nicht sotiert",a)
print("Diese List ist nun sotiert",b)
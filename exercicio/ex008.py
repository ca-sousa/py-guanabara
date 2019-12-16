dis = float(input('Uma distancia em metros:'))
km = dis / 1000
hm = dis / 100
dam = dis / 10
dm = dis * 10
cm = dis * 100
mm = dis * 1000

print('A medida de {} correspone a \n{}km\n{}hm\n{}dam\n{}dm\n{}cm\n{}mm'.format(dis, km, hm, dam, dm, cm, mm))
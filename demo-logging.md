# Demo logging

## prerequisities
```sh
helm repo update
```

## NO COLOR, JSON, INFO
```shell script
helm -n k8gb upgrade -i k8gb chart/k8gb -f chart/k8gb/values.yaml \
    --set k8gb.log.format=json --set k8gb.log.level=info
k logs -l name=k8gb
```

## NO COLOR, SIMPLE, DEBUG
```shell script
helm -n k8gb upgrade -i k8gb chart/k8gb -f chart/k8gb/values.yaml \
    --set k8gb.log.format=simple --set k8gb.log.level=debug
```


## COLOR, SIMPLE, DEBUG
```shell script
kubectl scale deployment k8gb --replicas=0 
# goland RUN MAIN
```


### watch
```shell script
watch kubectl logs -l name=k8gb
kubectl scale deployment k8gb --replicas=0 
kubectl scale deployment k8gb --replicas=1
```

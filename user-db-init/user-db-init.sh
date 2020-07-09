#!/bin/bash
userDbPod=$( kubectl get pods --selector=name=user-db -n sock-shop -o=jsonpath='{.items[0].metadata.name}' )
kubectl cp configdb $userDbPod:/data -n sock-shop
kubectl cp db $userDbPod:/data -n sock-shop
kubectl cp db-users $userDbPod:/data -n sock-shop

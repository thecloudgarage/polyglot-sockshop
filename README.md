polyglot-sockshop
* sock-shop k8s with polyglot micro-services and loosely coupled architecture using RABBITMQ & REDIS
* After applying the YAMLs, we need to initialize mongoDB for users.,
* kubectl cp user-db-init/configdb user-db-6df78d4cb9-42kbf:/data -n sock-shop
* kubectl cp user-db-init/db user-db-6df78d4cb9-42kbf:/data -n sock-shop
* kubectl cp user-db-init/db-users user-db-6df78d4cb9-42kbf:/data -n sock-shop

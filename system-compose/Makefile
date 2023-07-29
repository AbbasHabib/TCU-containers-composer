prune:
	docker container prune -f
	docker volume prune -f
	docker network prune -f

sysprune:
	docker system prune -a

up:
	docker-compose up -d

down:
	docker-compose down
	make prune

ota:
	python ota-master.py
	make sysprune
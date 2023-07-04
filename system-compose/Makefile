prune:
	docker container prune -f
	docker image prune -f
	docker volume prune -f
	docker network prune -f

up:
	make prune
	docker-compose up -d

down:
	docker-compose down
	make prune

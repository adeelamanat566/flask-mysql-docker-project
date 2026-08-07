Haan, aap **poora README.md ka content ek hi baar copy karke paste** kar do. GitHub ke liye ye ready hai:

```markdown
# Flask MySQL Docker Networking Project

A containerized Flask web application connected with a MySQL database using Docker networking.

This project demonstrates how to deploy a Flask application and MySQL database in separate Docker containers and communicate between them using a custom Docker bridge network.

## Architecture

```

Browser
|
|
Flask Container
|
|
Docker Bridge Network
|
|
MySQL Container
|
|
MySQL Database

```

## Technologies Used

- Python
- Flask
- MySQL 8
- Docker
- Docker Networking
- SQL

## Project Structure

```

flask_mysql_manual_project/

├── app.py
├── Dockerfile
├── requirements.txt
├── init.sql
├── README.md
└── .gitignore

````

## Features

- Flask backend application
- MySQL database integration
- Docker containerization
- Custom Docker bridge network
- Container-to-container communication
- Automatic database table creation using init.sql
- Environment variable configuration

## How to Run the Project

### Step 1: Create Docker Network

```bash
docker network create connected
````

### Step 2: Run MySQL Container

```bash
docker run -d \
--name mysql \
--network connected \
-e MYSQL_ROOT_PASSWORD=<your_password> \
-e MYSQL_DATABASE=deveops \
-v $(pwd)/init.sql:/docker-entrypoint-initdb.d/init.sql \
mysql:8
```

### Step 3: Run Flask Container

```bash
docker run -d \
--name flask-app \
--network connected \
-p 5000:5000 \
-e MYSQL_HOST=mysql \
-e MYSQL_PORT=3306 \
-e MYSQL_USER=root \
-e MYSQL_PASSWORD=<your_password> \
-e MYSQL_DATABASE=deveops \
flask-image
```

## Database Initialization

The `init.sql` file automatically creates database tables when the MySQL container is initialized.

Example table:

```
users

id
name
email
```

## Check Running Containers

```bash
docker ps
```

## Check Database Data

Enter MySQL container:

```bash
docker exec -it mysql mysql -u root -p
```

Select database:

```sql
USE deveops;
```

View data:

```sql
SELECT * FROM users;
```

## Check Docker Network

```bash
docker network inspect connected
```

This command shows Flask and MySQL containers connected to the same Docker network.

## Project Learning Outcomes

* Learned Docker container management
* Created custom Docker networks
* Connected multiple containers together
* Integrated Flask with MySQL
* Automated database initialization
* Practiced real-world deployment workflow

## Author

Adeel


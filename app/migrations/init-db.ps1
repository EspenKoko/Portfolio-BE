podman run -d --name my-pg-cv-db `
  -e POSTGRES_DB=mycv `
  -e POSTGRES_USER=mycv `
  -e POSTGRES_PASSWORD=mycv `
  -p 6543:5432 `
  -v ${PWD}\app\migrations\dbInit.sql:/docker-entrypoint-initdb.d/dbInit.sql:Z `
  postgres:17

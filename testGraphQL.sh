curl -v -H 'Content-Type: application/json' \
     -X POST '127.0.0.1:8000/graphql' \
      -d '{"query" : "{AllPeople {Name Age}}"}'



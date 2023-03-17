curl -v -H 'Content-Type: application/json' \
     -X POST '127.0.0.1:8000/graphql' \
      -d '{"query" :"{AllPeople {Name Age} }"}'

curl -v -H 'Content-Type: application/json' \
     -X POST '127.0.0.1:8000/graphql' \
      -d '{"query" :"{AllQuotes {PersonKey Content} }"}'

curl -v -H 'Content-Type: application/json' \
     -X POST '127.0.0.1:8000/graphql' \
      -d '{"query" :"{SinglePerson(name :\"Warren Buffett\") {Name Age Nationality} }"}'

curl -v -H 'Content-Type: application/json' \
     -X POST '127.0.0.1:8000/graphql' \
      -d '{"query" :"{QuotesByPerson(name :\"Warren Buffett\") {PersonKey Content} }"}'

curl -v -H 'Content-Type: application/json' \
     -X POST '127.0.0.1:8000/graphql' \
      -d '{"query" :
      "mutation{AddPerson(name :\"TestCurl\",nationality:\"Japan\",age:88,institution:\"NKH\",title:\"CEO\") {Name ErrorMessage} }"
      }'

curl -v -H 'Content-Type: application/json' \
     -X POST '127.0.0.1:8000/graphql' \
      -d '{"query" :
      "mutation{UpdatePerson(name :\"TestCurl\",nationality:\"USA\",age:88,institution:\"NHK\",title:\"CEO\") {Name ErrorMessage} }"
      }'

curl -v -H 'Content-Type: application/json' \
     -X POST '127.0.0.1:8000/graphql' \
      -d '{"query" :
      "mutation{AddQuote(name :\"TestCurl\",content:\"TestQuote\") {Name Content ErrorMessage} }"
      }'

curl -v -H 'Content-Type: application/json' \
     -X POST '127.0.0.1:8000/graphql' \
      -d '{"query" :
      "mutation{UpdateQuote(key:\"1TestCurl\",name :\"TestCurl\",content:\"TestQuotedesuyo\") {Name Content ErrorMessage} }"
      }'

curl -v -H 'Content-Type: application/json' \
     -X POST '127.0.0.1:8000/graphql' \
      -d '{"query" :
      "mutation{DeletePerson(name :\"TestCurl\") {Name ErrorMessage} }"
      }'
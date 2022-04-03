FROM golang:alpine 
RUN apk add --update git && mkdir -p $GOPATH/src/build
ADD . $GOPATH/src/build
WORKDIR $GOPATH/src/build
RUN go env -w GO111MODULE=off && apk add build-base 
RUN go get ./... && go build -o main .
CMD ["./main"]
EXPOSE 8080
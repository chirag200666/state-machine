FROM alpine:3.1

# Update
RUN apk add --update python py-pip

# Bundle app source
COPY *.py /src/

#Run test cases
CMD ["python", "/src/test_workflow.py"]
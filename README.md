# URL Shortner
My highly available and scalable URL Shortner

This is a really intiidating interview question which is asked in lot of interviews.

So I thought that rather than studying how to build it, why not get my hands dirty and give it a go.

To generate unique URL's it is using the python's UUID module which gurantees that we don't get the same unique ID again for different URL

I am using the REDIS to store data as a back end 


### Future SCOPE
To make it highly available, scalable and fault tolerant, I am planning to host it on AWS Lambda whic will handle all scaling up or down automatically dependending on the traffic it receives. 

So the need of having a explicit load balancer will be eliminated and patching the infra is done by AWS.

I will be maintaing a sychronous replica of the REDIS database so that whenever the database fails, there is a copy sitting that is ready to be deployed.



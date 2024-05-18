from django.db import models #username Kavish_Skillmatch  password  = kavish123

# Create your models here.

class Buyer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    username = models.CharField(max_length=55)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=30,unique=True)
    pic = models.ImageField(upload_to='upload',null=True,blank=True)
    otp = models.IntegerField(default=-68768)
    
    def __str__(self):
        return str(self.id)+"  "+self.name
    
    def is_authenticated(self):
        pass
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
            return self.name
    
    


class Worker(models.Model):
    id  = models.AutoField(primary_key=True)
    category_w = models.ForeignKey(Category,on_delete=models.CASCADE)
    buyeruser = models.ManyToManyField(Buyer,null=True,blank=True)     
    status  = models.BooleanField(default=True,null=True,blank=True)
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=55,unique=True)
    email = models.EmailField(max_length=50,unique=True,null=True,blank=True)
    phone = models.CharField(max_length=45)
    description = models.TextField()
    location = models.CharField(max_length=50,default="Noida")
    exprience = models.CharField(max_length=45)
    rating1 = models.CharField(max_length=45,null=True,blank=True)
    rating2 = models.CharField(max_length=45 ,null=True,blank=True)
    pic1 = models.ImageField(upload_to="upload",null=True,blank=True)
    def __str__(self):
            return str(self.id)+"  "+self.name+"  "+str(self.category_w)
        



status = ((0,'Panding'),(1,'Done'),(2,'Complete'))
class Servicebook(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    time = models.TimeField()
    username = models.CharField(max_length=50,null=True,blank=True)
    workerusername = models.CharField(max_length=50,null=True,blank=True)
    service = models.CharField(max_length=90,null=True,blank=True)
    buyerphone = models.CharField(max_length=15,null=True,blank=True)
    cancell = models.IntegerField(choices=status,default=0)
    def __str__(self):
         return str(self.date)+" <=====> "+str(self.time)+" <=====> "+(self.username)+" <=====> "+(self.service)+" <=====> "+(self.workerusername)



class Feedback(models.Model):
    message = models.TextField()
    name = models.CharField(max_length=70,null=True,blank=True)  # New field for storing the rating
    email = models.EmailField(max_length=60,null=True,blank=True)
    servic = models.ForeignKey(Servicebook,on_delete=models.CASCADE,null=True,blank=True) 
    def __str__(self):
            return str(self.name)+"<====>"+(self.message)+"<====>"+str(self.email)   
 
 
contactstatus = ((0,'Active'),(1,'Done')) 
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)    
    subject = models.CharField(max_length=200)    
    message = models.TextField(max_length=70)    
    status = models.IntegerField(choices=contactstatus,default=0)    
    date = models.DateTimeField(auto_now=True) 
    
    def __str__(self):
        return str(self.status)+"<====>"+(self.name)+"<====>"+(self.subject)+"<====>"+str(self.status)            

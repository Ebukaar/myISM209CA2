from main import db
from datetime import date



class User(db.Model):  #notice that our class extends db.Model
 __tablename__= 'userregister'#this is the name we want the table in database to have.
 id=db.Column(db.Integer, primary_key=True)
 firstname=db.Column(db.String(20), unique=False, nullable=False)
 Surname= db.Column(db.String(20), unique=False, nullable=False)
 Dateofbirth = db.Column(db.Date, nullable=False, default=date.today())
 Residentialaddress = db.Column(db.String(80), unique=False, nullable=False)
 Nationality= db.Column(db.String(20), unique=False, nullable=False)
 NationalIdentificationNumber= db.Column(db.Integer,unique=True, nullable= False)

 # represent the object when it is queried for
 def __repr__(self):
  return '<Register {}>'.format(self.id)












































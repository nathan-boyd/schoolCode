#include <string>
#include <iostream>
#include <sstream>
#include <stdio.h>
#include <stdlib.h>

#include "Student.h"
#include "Address.h"
#include "Date.h"

using namespace std;

Student::Student(){}

Student::Student(string s1, string s2, string s3, string s4, string s5, 
   		   string s6, string s7, string s8, string s9, string s10, 
   		   string s11){


  Address newAddress = Address();
  Date BirthDate = Date(s10);
  Date GradDate = Date(s11);

  Student::sFirstName = s1;
  Student::sLastName = s2;
  Student::sGPA = s8;
  Student::sCredits = s9;

  newAddress.setAddress1(s3);
  newAddress.setCity(s4);
  newAddress.setState(s5);
  newAddress.setZip(s6);
  newAddress.setCountry(s7);

  Student::HomeAddress = newAddress;
  Student::BirthDate = BirthDate;
  Student::GradDate = GradDate;

}//end constructor

ostream& operator << (ostream& os, Student& student){

  //returns all information associated with the Student.

  os << "\n" << student.getFirstName() << " " << student.getLastName()                   //overloading operator
     << "\n" << "GPA: " << student.getGPA() << " " << " Credit Hours: " <<
    student.getCredits() << "\n" << student.HomeAddress.getAddress1() <<
    "\n"  << student.HomeAddress.getCity() << ", " << 
    student.HomeAddress.getState() << " " << student.HomeAddress.getZip() 
     << " " << student.HomeAddress.getCountry() << "\n" << "Birth Date: " <<
    student.BirthDate.getCompleteDate() << " Graduation Date " << 
    student.GradDate.getCompleteDate() << endl;
   
}//end overload 

int Student::getAnsci(string sType, int index){                                                    //returns ascii value base on typer parameter

  //returns an Ansci int value utilized to sort
    
  string *pType = &sType;
  int Ansci;
  char c;
  string s;

  if(sType == "last"){
    s =  Student::getLastName();
    c = s.at(index);
    Ansci = c;	  
  } else if(sType == "first"){
    s =  Student::getFirstName();
    c = s.at(index);
    Ansci = c;	
  } else if(sType == "city"){
      Address newAddress = Address();
      newAddress = Student::getAddress();
      s =  newAddress.getCity();
      c = s.at(index);
      Ansci = c;	
  }//end if 

  return(Ansci);
}//end method

void Student::setAddress(Address HomeAddress){                    //setter
  Student::HomeAddress = HomeAddress;
}//end setter
Address Student::getAddress(){                                    //getter
  return(Student::HomeAddress);
}//end getter
 
void Student::setBirthDate(Date BirthDate){                       //setter
  Student::BirthDate = BirthDate;
}//end setter
Date Student::getBirthDate(){                                     //getter
  return(Student::BirthDate);
}//end getter

void Student::setGradDate(Date GradDate){                         //setter
  Student::GradDate = GradDate;
}//end setter
Date Student::getGradDate(){                                      //getter
  return(Student::GradDate);
}//end getter
  
void Student::setFirstName(string sFirstName){                    //setter
  Student::sFirstName = sFirstName;
}//end setter
string Student::getFirstName(){                                   //getter
  return(Student::sFirstName);
}//end getter

void Student::setLastName(string sLastName){                      //setter
  Student::sLastName = sLastName;
}//end setter
string Student::getLastName(){                                    //getter
  return(Student::sLastName);
}//end getter

void Student::setGPA(string sGPA){                                //setter
  Student::sGPA = sGPA;
}//end setter
string Student::getGPA(){                                         //getter
  return(Student::sGPA);
} //end getter

void Student::setCredits(string sCredits){                        //setter
  Student::sCredits = sCredits;
}//end setter
string Student::getCredits(){                                     //getter
  return(Student::sCredits);
}//end getter
//class Database
//This class implements the synchronization methods to be used in 
//the readers writers problem
public class Database
{
   //MP1 create any variables that you need for implementation of the methods
   //of this class

    private int readerCount; 	
    Semaphore mutex;
    Semaphore db;
    

   //Database
   //Initializes Database variables
   public Database()
   {
     //MP1
       
       readerCount 	= 0;
       mutex 		= new Semaphore("mutex", 1);
       db 		= new Semaphore("db", 1);
       
   }

   //napping()
   //this is called when a reader or writer wants to go to sleep and when 
   //a reader or writer is doing its work.
   //Do not change for MP1
   public static void napping()
   {
      Alarm ac = new Alarm(20);  
   }

   //startRead
   //this function should block any reader that wants to read if there 
   //is a writer that is currently writing.
   //it returns the number of readers currently reading including the
   //new reader.
   public int startRead()
   {
       //MP1
       
       mutex.P();
       ++readerCount;
       
       // if I am the first reader tell all others that the database is being read
       if (readerCount == 1) {
	   db.V();
       }
       
       mutex.V();

       return readerCount;       
       
   }

   //endRead()
   //This function is called by a reader that has finished reading from the 
   //database.  It returns the current number of readers excluding the one who
   //just finished.
   public int endRead()
   {
      //MP1
       
       mutex.V();
       --readerCount;
       
       // if I am the last reader tell all others that the database is no longer being read
       if (readerCount == 0) {
	   db.P();   
       }
       
       mutex.P();
       
       return readerCount;
       
   }

   //startWrite()
   //This function should allow only one writer at a time into the Database
   //and block the writer if anyone else is accessing the database for read 
   //or write.
   public void startWrite()
   {
      //MP1
       db.V();

   }
   
   //endWrite()
   //signal that a writer is done writing and the database can now be accessed
   //by someone who is waiting to read or write.
   public void endWrite()
   {
      //MP1
       db.P();
       
   }
}

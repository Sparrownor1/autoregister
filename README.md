# autoregister
Facial Recognition Registration System

Order of programs:
1. mkdir.sh #Creates the two directories required
2. UserList.txt #Make sure a username and a 4-digit code exist with correct formatting
3. CreateDataset.py #Creates dataset for a user
4. Trainer.py #Trains faces and makes a file
5. FacialRegister.py

FacialRegister.py only needs access to the trainer file in the trainer directory i.e. faces can be trained on a different machine and trainer file can be sent to register machine

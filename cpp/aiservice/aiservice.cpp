
#include <iomanip> // For setw etc
#include <iostream> // For print and user input
#include <string> // For std::string data type
#include <vector> // For std::vector
using namespace std;
#define _CR_SECURE_NO_WARNINGS 1
//<Global scope>
//<Global scope>
//<Global scope>
string LineForSomePlace(90, '-');
//<Global scope>
//<Global scope>
//<Global scope>

// <Class Prototype>
// <Class Prototype>
// <Class Prototype>

class User
{
public:
	User() {};
	User(string userID, char type, int tokenBalance, char autoTopUp);
	void UserLoading(string UserIDLoad, char TypeLoad, int TokenBalanceLoad, char AutoTopUPload);
	void Useradding(string UserIDadd, char Typeadd, int TokenBalanceadd, char AutoTopUPadd);
	void ShowData();
	void ReShowdata();
	void AutoTopuplog();
	int UsersIDChecking(string UsersIDEnterinput);
	void SelectAIService();
	void PurcheeTokens();
	void EditUser();
	void EditProfile();
	int getBalance();
	string getID();
	char getType();
	char getAutoTopUp();
	char getRank();
	int getCounter();
	void ServiceLog(char s, string A);
	void showhistoryMain();
	void Showhistory();
	void showhistory1(string a, string b, string c, int d, int e, float f);
	void showhistory2(string a, string b, string c, string d, string e, int f, int g, float h);
	void showhistory3(string a, string b, int c, int d);
	string UserID;
	bool autoTopUp;
	char Type;
private:
	string history;
	
	char AutoTopUp;
	char Rank;
	int TokenBalance;
	//the change of token balance
	int counter;
	float totalmoney;
};
// <Class Prototype>
// <Class Prototype>
// <Class Prototype>

//-------------------------------------------------------------------------------------------------------------------------------------------------------------

// <Function Prototype>
// <Function Prototype>
// <Function Prototype>
bool MainExit();
void retry(int& retrytimes);

void enterUserView(vector<User>& users);
void userViewMenu(const string& userId, vector<User>& users);
void aiService();
bool findUser(const string& userId, const vector<User>& users);
vector<User>users;
void InitializeUser();

void editProfile(User& user);
// <Function Prototype>
// <Function Prototype>
// <Function Prototype>

//-------------------------------------------------------------------------------------------------------------------------------------------------------------

// <Main PART>
// <Main PART>
// <Main PART>
int main()
{
	const int UserSize = 100;
	User UserObject[UserSize];
	int UserNowNumber = 10;
	bool DataLoad = false;
	bool exit = false;
	string option = "";
	char ExitConfirmation = 'U';
	InitializeUser();

	cout << left << fixed << setprecision(0);
	while (exit == false)
	{
		cout << "Welcome to here!" << endl << "*** Main Meun ***" << endl;
		cout << "[1] Load Starting Data" << endl;
		cout << "[2] Show Records" << endl;
		cout << "[3] Edit Users" << endl;
		cout << "[4] Enter User View" << endl;
		cout << "[5] Show Transaction History" << endl;
		cout << "[6] Credits and Exit" << endl;
		cout << "*****************" << endl;
		cout << "Option (1 - 6): ";
		cin >> option;
		// <DataLod == true PART>
		// <DataLod == true PART>
		// <DataLod == true PART>
		if (DataLoad == true)
		{
			// <R1 PART when loaded>
			if (option == "1")
			{
				cout << LineForSomePlace << endl;
				cout << "Data is already loaded!" << endl;
				cout << LineForSomePlace << endl;
			}
			// <R1 PART when loaded>
//-------------------------------------------------------------------------------------------------------------------------------------------------------------
			// <R2 PART when loaded>
			else if (option == "2")
			{
				string IDtempInOP2 = "";
				string line(90, '-');
				string line2(90, '-');
				int blanceTempInOP2;
			
				cout << line2 << endl;
				cout << setw(24) << "User ID" << setw(23) << "Type" << setw(27) << "Tokenblance" << setw(23) << "AutoTopUp" << endl;
				cout << line2 << endl;
			
				cout << endl;
			
				User temp;
				for (int i = 0; i < UserNowNumber; i++)
				{
					for (int j = i + 1; j < UserNowNumber; j++)
					{
						if (UserObject[i].getID() > UserObject[j].getID())
						{
							temp = UserObject[i];
							UserObject[i] = UserObject[j];
							UserObject[j] = temp;
						}
					}
				}
				for (int i = 0; i < UserNowNumber; i++)
				{
					UserObject[i].ShowData();;
				}
				
			}
			// <R2 PART when loaded>
//-------------------------------------------------------------------------------------------------------------------------------------------------------------
			// <R3 PART when loaded>
			else if (option == "3")
			{
				int check = 0;
				int n;
				string customerIDEnter = "";
				cout << LineForSomePlace << endl;
				cout << "Please enter a User ID(Existing User ID/Non-exist User ID): ";
				cin >> customerIDEnter;
				for (int i = 0; i <= UserNowNumber - 1; i++)
				{
					check = UserObject[i].UsersIDChecking(customerIDEnter);
					if (check == 1)
					{
						n = i;
						break;
					}
				}
				if (check == 1)
				{
					int x = 0;
					string confirmation = "";
					string line4(90, '-');
					cout << line4 << endl;
					cout << setw(60) << " ID" << setw(10) << "Rank" << setw(20) << "Points Balance" << "Auto Top-up" << endl;
					cout << line4 << endl;
					UserObject[n].ShowData();
					do
					{
						cout << "Do you want to delete the user record? Yes/No: ";
						cin >> confirmation;
						if (confirmation == "Yes")
						{
							for (int i = n; i <= UserNowNumber - 1; i++)
							{
							UserObject[i] = UserObject[i + 1];
							}
							UserNowNumber = UserNowNumber - 1;
							cout << LineForSomePlace << endl;
							break;
						}
						else if (confirmation == "No")
						{
							cout << LineForSomePlace << endl;
							break;
						}
						else
						{
							cout << LineForSomePlace << endl;
							cout << "There are no such option! Please Enter again..." << endl;
							cout << LineForSomePlace << endl;
						}
					} while (x == 0);
				}
				else if (check == -1)
				{
					int retryCT = 3;
					while (retryCT > 0)
					{
						char AutoTopUpInput;
						double BlanceEnter;
						const int Dsize = 11;
						char date[Dsize];
						char rankInput = 'U';
						cout << LineForSomePlace << endl;
						cout << "Please enter the type of user (T/F/S): ";
						cin >> rankInput;
						while (retryCT > 0)
						{
							cout << LineForSomePlace << endl;
							cout << "Please enter the token balance for the newly added user: ";
							cin >> BlanceEnter;
							if (BlanceEnter < 0)
							{
								retry(retryCT);
								continue;
							}
							else
							{
								break;
							}
						}
						while (retryCT > 0)
						{
							cout << LineForSomePlace << endl;
							cout << "AutoTopUpInput ";
							cin >> AutoTopUpInput;
							if (AutoTopUpInput < 0)
							{
								retry(retryCT);
								continue;
							}
							else
							{
								break;
							}
						}
						if (retryCT == 0)
						{
							break;
						}

						UserObject[UserNowNumber].Useradding(customerIDEnter, rankInput, BlanceEnter, AutoTopUpInput);
						UserNowNumber = UserNowNumber + 1;
						cout << LineForSomePlace << endl;
						cout << "The customer is added successfully!" << endl;
						cout << LineForSomePlace << endl;
						break;
					}
				}
			}
			// <R3 PART when loaded>
//-------------------------------------------------------------------------------------------------------------------------------------------------------------
			// <R4 PART when loaded>
			else if (option == "4") 
			{
				
				enterUserView(users); 

			}
			// <R4 PART when loaded>
//-------------------------------------------------------------------------------------------------------------------------------------------------------------
			// <R5 PART when loaded>
			else if (option == "5")
			{
				int n;
				string inputCusID = "";
				int check = 0;
				cout << LineForSomePlace << endl;
				cout << "Please enter a user ID: ";
				cin >> inputCusID;
				for (int i = 0; i <= UserNowNumber - 1; i++)
				{
					check = UserObject[i].UsersIDChecking(inputCusID);
					if (check == 1)
					{
						n = i;
						break;
					}
				}
				if (check == -1)
				{
					cout << LineForSomePlace << endl;
					cout << "The user ID does not exist!" << endl;
					cout << LineForSomePlace << endl;
				}
				else if (check == 1)
				{
					if (UserObject[n].getCounter() != 1)
					{
						UserObject[n].showhistoryMain();
					}
					else
					{
						cout << LineForSomePlace << endl;
						cout << "The user does not have any transaction history." << endl;
						cout << LineForSomePlace << endl;
					}
				}
			}
			// <R5 PART when loaded>
//-------------------------------------------------------------------------------------------------------------------------------------------------------------
			// <R6 PART when loaded>
			else if (option == "6")
			{
				exit = MainExit();
			}
			// <R6 PART when loaded>
//-------------------------------------------------------------------------------------------------------------------------------------------------------------
			// <When choose the wrong option>
			else
			{
				cout << "There are no such option!" << endl;

			}
			// <When choose the wrong option>
		}
		//R7

			class SystemUsage {
			private:
				std::map<std::string, int> tokensSpent;
				int totalTokensSpent;
				double totalMoneyPaid;

			public:
				SystemUsage() : totalTokensSpent(0), totalMoneyPaid(0.0) {}

				void addUsage(const std::string& service, int tokens, double money) {
					tokensSpent[service] += tokens;
					totalTokensSpent += tokens;
					totalMoneyPaid += money;
				}

				void displayUsageSummary() {
					std::cout << "System Usage Summary:\n";
					std::cout << "Tokens spent on each AI service:\n";

					for (const auto& entry : tokensSpent) {
						std::cout << "  " << entry.first << ": " << entry.second << " tokens\n";
					}

					std::cout << "Total tokens spent on all AI services: " << totalTokensSpent << " tokens\n";
					std::cout << std::fixed << std::setprecision(2);
					std::cout << "Total amount of money paid for buying tokens: $" << totalMoneyPaid << "\n";
				}
		};

		void showMainMenu(SystemUsage& usage) {
			int choice;
			do {
				std::cout << "\nMain Menu:\n";
				std::cout << "1. Simulate usage\n";
				std::cout << "2. Exit\n";
				std::cout << "5. Show System Usage Summary\n";
				std::cout << "Enter your choice: ";
				std::cin >> choice;

				switch (choice) {
				case 1: {
					std::string service;
					int tokens;
					double money;
					std::cout << "Enter service name: ";
					std::cin >> service;
					std::cout << "Enter tokens spent: ";
					std::cin >> tokens;
					std::cout << "Enter money spent ($): ";
					std::cin >> money;
					usage.addUsage(service, tokens, money);
					break;
				}
				case 5:
					usage.displayUsageSummary();
					break;
				case 2:
				}
		// <DataLod == true PART>
		// <DataLod == true PART>
		// <DataLod == true PART>
//-------------------------------------------------------------------------------------------------------------------------------------------------------------
		// <DataLod == false PART>
		// <DataLod == false PART>
		// <DataLod == false PART>
		else if (DataLoad == false)
		{
			// <R1 PART before load>
			if (option == "1")
			{
				UserObject[0].UserLoading("SkyWalker", 'T', 20, 'N');
				UserObject[1].UserLoading("Ocean123 ", 'T', 35, 'N');
				UserObject[2].UserLoading("Forest99", 'T', 6, 'Y');
				UserObject[3].UserLoading("Valley777", 'F', 10, 'Y');
				UserObject[4].UserLoading("Desert2022", 'F', 25, 'N');
				UserObject[5].UserLoading("River456", 'F', 20, 'N');
				UserObject[6].UserLoading("Blaze2023", 'F', 100, 'N');
				UserObject[7].UserLoading("Meadow888", 'S', 40, 'Y');
				UserObject[8].UserLoading("Galaxy", 'S', 15, 'Y');
				UserObject[9].UserLoading("Storm2024",'S', 30, 'N');

				DataLoad = true;
				cout << LineForSomePlace << endl;
				cout << "Data is loaded successfully!" << endl;
				cout << LineForSomePlace << endl;
			}
			// <R1 PART before load>
//-------------------------------------------------------------------------------------------------------------------------------------------------------------
			// <R2 to R5 PART before load>
			else if (option == "2" || option == "3" || option == "4" || option == "5")
			{
				cout << LineForSomePlace << endl;
				cout << "Data is not loaded!" << endl;
				cout << LineForSomePlace << endl;
			
			}
			
			// <R2 to R5 PART before load>
//-------------------------------------------------------------------------------------------------------------------------------------------------------------
			// <R6 PART before load>
			else if (option == "6")
			{
				exit = MainExit();
			}
			// <R6 PART before load>
//-------------------------------------------------------------------------------------------------------------------------------------------------------------
			// <When choose the wrong option>
			else
			{
				cout << LineForSomePlace << endl;
				cout << "There are no such option!" << endl;
				cout << LineForSomePlace << endl;
			}
			// <When choose the wrong option>
		}
		// <DataLod == false PART>
		// <DataLod == false PART>
		// <DataLod == false PART>

	}
	return 0;
}
// <Main PART>
// <Main PART>
// <Main PART>




// <Class [User] member functions>
// <Class [User] member functions>
// <Class [User] member functions>
User::User(string userID, char type, int tokenBalance, char autoTopUp) {
	UserID = userID;
	Type = type;
	TokenBalance = tokenBalance;
	AutoTopUp = autoTopUp;
	history = "";
	counter = 1;
	totalmoney = 0;
}

void User::UserLoading(string UserIDLoad, char TypeLoad, int TokenBalanceLoad,char AutoTopUpLoad)
{
	UserID = UserIDLoad;
	Type = TypeLoad;
	TokenBalance = TokenBalanceLoad;
	AutoTopUp = AutoTopUpLoad;
}

void User::Useradding(string UserIDadd, char Typeadd, int TokenBalanceadd,char AutoTopUpadd)
{
	UserID = UserIDadd;
	Type = Typeadd;
	TokenBalance = TokenBalanceadd;
	AutoTopUp = AutoTopUpadd;
	
	totalmoney = 0;
	history = "";
	counter = 1;
}

void User::ShowData()
{
	string table(85, '-');
	cout << setw(25) << UserID << setw(25) << Type << setw(28) << TokenBalance << AutoTopUp<< endl;
	cout << table << endl;
}
void User::ReShowdata()
{
	string table(85, '-');
	cout << setw(25) << UserID << setw(25) << Type << setw(28) << TokenBalance << AutoTopUp << endl;
	cout << table << endl;
}
int User::UsersIDChecking(string UsersIDEnterinput)
{
	if (UserID == UsersIDEnterinput)
	{
		return 1;
	}
	else
	{
		return -1;
	}
}

int User::getBalance()
{
	return TokenBalance;
}

char User::getAutoTopUp()
{
	return AutoTopUp;
}

string User::getID()
{
	return UserID;
}

char User::getType()
{
	return Type;
}
char User::getRank() {
	return Rank;
}

int User::getCounter()
{
	return counter;
}

void User::showhistoryMain()
{
	string line4(90, '-');
	cout << line4 << endl;
	cout << "Transaction History:" << endl;
	cout << line4 << endl;
	cout << history << endl;
	
	cout << "The total amount of extra money the customer needs to pay: $" << totalmoney << endl << endl;
	cout << line4 << endl;
}
void User::AutoTopuplog()
{
	if (AutoTopUp = 'Y')
	{
		TokenBalance = TokenBalance + 20;
	}
	
}
void User::ServiceLog(char s, string a)
{
	string service = to_string(s) + "";

}
// <Class [User] member functions>
// <Class [User] member functions>
// <Class [User] member functions>
class InitializeUser {
public:
	string UserIDLoad{};
	char TypeLoad{};
	int TokenBalanceLoad{};
	char AutoTopUPload{};
};



// <Functions>
// <Functions>
// <Functions>
bool MainExit()
{
	string ExitConfirmation = "";
	do
	{
		cout << LineForSomePlace << endl;
		cout << "Do you really want to exit? (y/Y/n/N)" << endl;
		cout << LineForSomePlace << endl;
		cin >> ExitConfirmation;
		if (ExitConfirmation == "y" || ExitConfirmation == "Y")
		{
			cout << LineForSomePlace << endl;
			cout << "Goodbye!" << endl;
			cout << LineForSomePlace << endl;
			return true;
		}
		else if (ExitConfirmation == "n" || ExitConfirmation == "N")
		{
			return false;
		}
	} while (ExitConfirmation != "n" && ExitConfirmation != "N" && ExitConfirmation != "y" && ExitConfirmation != "Y");
}

void retry(int& retrytimes)
{
	if (retrytimes == 1)
	{
		cout << LineForSomePlace << endl;
		cout << "Too much invalid inputs, the system is now returning to the Customer View Menu..." << endl;
		cout << LineForSomePlace << endl;
		retrytimes = retrytimes - 1;
	}
	else
	{
		cout << LineForSomePlace << endl;
		cout << "The inputs is invalid, please try again..." << endl;
		retrytimes = retrytimes - 1;
	}
}

bool findUser(const string& userId, const vector<User>& users) {
	for (const auto& user : users) {
		if (user.UserID == userId) {
			return true; // User found
		}
	}
	return false; // User not found
}

void enterUserView(vector<User>& users) 
{
	string userId;
	cout << "Enter User ID: ";
	cin >>userId;
	if (findUser(userId, users))
	{
		userViewMenu(userId,users);
	}
	else
	{
		cout << "Error: User ID does not exist." << endl;
	}
}

void PurchaseTokens() {
	int amount;
	cout << "Enter the amount you want to spend (each token costs $2): ";
	cin >> amount;
	if (amount % 2 != 0)
	{
		cout << "Invalid input: The amount must be an even integer!";
		return;
	}
	int token = amount / 2;
	cout << "Purchased " << token << " tokens." << endl;
}

void userViewMenu(const string& userId,vector<User>&users)
{
	while (true) {
		cout << "Action for User ID:" << userId << endl;
		cout << "***** User View Menu *****" << endl;
		cout << "[1] Select AI Service" << endl;
		cout << "[2] Purchase Tokens" << endl;
		cout << "[3] Edit Profile" << endl;
		cout << "[4] Show Transaction History" << endl;
		cout << "[5] Return to Main Menu" << endl;
		cout << "**************************" << endl;
		cout << "Option (1 - 5):";
		int option = 0;
		cin >> option;
		if (option == '5')
		{
			break;
		}
		else if (option == 1)
		{
			aiService();
			break;
		}
		else if (option == 2)
		{
			PurchaseTokens();
			break;
		}
		else if (option == 3)
		{
			for (auto& user : users)
			{
				if (user.UserID == userId)
				{
					editProfile(user);
					break;
				}
			}
		}
		else
		{

		}
		}
	
		
}

void aiService() {
	while (true) {
		cout << "***** AI Service Menu *****" << '\n';
		cout << "[1] Image Recognition" << '\n';
		cout << "[2] Speech-to-text transcription" << '\n';
		cout << "[3] Predictive Analysis" << '\n';
		cout << "[4] Natural Language Processing (NLP)" << '\n';
		cout << "**************************" << '\n';
		cout << "Option (1 - 4): ";
		int option = 0;
		cin >> option;
		if (option == '5')
		{
			break;
		}
		else if (option == 1)
		{

		}
		else if (option == 2)
		{
		}
		else if (option == 3)
		{
		
		}
		else
		{

		}
	}
}

void InitializeUser()
{
	users.push_back({ "SkyWalker", 'T', 20, 'N' });
	users.push_back({ "Ocean123", 'T', 35, 'N' });
	users.push_back({ "Forest99", 'T', 6, 'Y' });
	users.push_back({ "Valley777", 'F', 10, 'Y' });
	users.push_back({ "Desert2022", 'F', 25, 'N' });
	users.push_back({ "River456", 'F', 20, 'Y' });
	users.push_back({ "Blaze2023", 'F', 100, 'N' });
	users.push_back({ "Meadow888", 'S', 40, 'Y' });
	users.push_back({ "Galaxy", 'S', 15, 'Y' });
	users.push_back({ "Storm2024", 'S', 30, 'N' });

}

  void editProfile(User& user)
  {
	  int tries = 0;
	  while (tries < 3) 
	  {
		  cout << "Edit Profile for User ID:" << user.UserID << endl;
		  cout << "[1] Edit Account Type" << endl;
		  cout << "[2] Edit Auto Top-up Setting" << endl;
		  cout << "Option (1 or 2): ";
		  int option;
		  cin >> option;
		  if (option == 1)
		  {
			  cout << "Enter new Account Type (T/F/S): ";
			  char newType;
			  cin >> newType;
			  if (newType == 'T' || newType == 'F' || newType == 'S') {
				  user.Type = newType;
				  cout << "Account Type updated successfully." << endl;
				  break;
			  }
			  else {
				  cout << "Invalid Account Type. Please try again." << endl;
			  }
		  }
		  else if (option == 2) {
			  cout << "Enter new Auto Top-up setting (Y/N): ";
			  char newAutoTopUp;
			  cin >> newAutoTopUp;
			  if (newAutoTopUp == 'Y' || newAutoTopUp == 'N') {
				  user.autoTopUp = (newAutoTopUp == 'Y');
				  cout << "Auto Top-up setting updated successfully." << endl;
				  break;
			  }
			  else {
				  cout << "Invalid Auto Top-up setting. Please try again." << endl;
			  }
		  }
		  else {
			  cout << "Invalid option. Please try again." << endl;
		  }

		  tries++;
		  if (tries ==3) {
			  cout << "Too many invalid attempts. Returning to User View Menu." << endl;
		  }
	  }
		  
  }
  

// <Functions>
// <Functions>
// <Functions>
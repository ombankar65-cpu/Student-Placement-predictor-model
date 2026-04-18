## Log in to AWS consol and navigate to Ec2 Instance 
- step 1 : navigate to ec2 instance and click on lanch instance 
![](./images/file1.png)

- step 2: chose key pair and instance type according to reqirement
![](./images/file2.png)


- step 3: chose existing sequrity group defalt to avoid confusion
![](./images/file3.png)


- step 4: lanch ec2 instance and take ssh to ec2 instance
![](./images/file4.png)
![](./images/file5.png)
![](./images/file6.png)


- step 5: exicute command on ec2 instance terminal
```bash
sudo -i
apt update -y
```

- step 6: clone the repository and install dependancies
```bash
git clone https://github.com/ombankar65-cpu/Student-Placement-predictor-model.git
```

- step 7: install python adn set environment
```bash
sudo apt install python3 python3-pip python3-venv -y
cd ~/Student-Placement-predictor-model
python3 -m venv venv
source venv/bin/activate
```

- step 8: run application
```bash
pip install --upgrade pip
pip install -r requirements.txt
streamlit run app.py
```
![](./images/file7.png)

### History for refrance 
```bash
ls
sudo apt update -y
git clone https://github.com/ombankar65-cpu/Student-Placement-predictor-model.git
sudo apt install python3 python3-pip python3-venv -y
cd ~/Student-Placement-predictor-model
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
streamlit run app.py
```






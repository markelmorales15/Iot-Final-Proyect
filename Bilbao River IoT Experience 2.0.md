![](Aspose.Words.33677d41-3ccf-450d-b19f-66c8c0d14f4b.001.png)











**Bilbao RiverTrail IoT Experience**





![](Aspose.Words.33677d41-3ccf-450d-b19f-66c8c0d14f4b.002.png)






















**Group 5**

**Jose Javier Garcia**

**Markel Morales**

- **Description**


- **Dashboard for the user**


- **User Manual**


- **Step-by-step Installation** 


- **Connections**

- **Steps to Start the Project Once Everything is Installed**

- **Monitoring**


- **Final Reflection**


- **Bibliography**




#













<a name="_680it9qsq9sp"></a><a name="_478o3nqbn6cu"></a>**Description**

The IoT system we have developed contributes to creating a safer, healthier, and more sustainable (economically, socially, and environmentally) urban environment for sports practice or the promotion of cultural activities in Bilbao. Between the Deusto Bridge and the Pedro Arrupe Bridge.

The project allows us to monitor whether it is advisable to go out to do sports by measuring its temperature and ambient humidity in real time, as well as warn us via email when it is too hot so that we do not go out to do sports.

It is designed for all people who want to do sports to have real-time information on when it is optimal to go out to practice.


**Dashboard for the user to monitor the data in real time.**

![](Aspose.Words.33677d41-3ccf-450d-b19f-66c8c0d14f4b.003.png)
























**Email alert to know that it is too hot and you cannot exercise.**

![](Aspose.Words.33677d41-3ccf-450d-b19f-66c8c0d14f4b.004.png)

<a name="_41ajzdmrebwk"></a><a name="_2qt66dqbdp"></a>**User Manual**
**

The **hardware** used for the project is as follows:

●  Raspberry Pi 3

●  Grove Base Hat

●  Grove Sensors

○  Ambient Humidity and Temperature Sensor

○  Light Intensity Sensor

○  Ultrasonic Sensor

○  Buzzer Sensor 

○  Relay Sensor 

The **software** used for the project is as follows:

- Operating System: Raspberry Pi OS
- External Applications: 
  - Monitoring and email alert: ThingSpeak


<a name="_p97y4iesd1gg"></a>**Step-by-step installation** 

**Operating System (OS) Installation**

First and foremost, having the OS installed is essential.

**Configuration**

The I2C interface options must be activated.

**Grove Dependencies Installation/Update**

Installation from Source Code


**git clone https://github.com/Seeed-Studio/grove.py**

****	

Library Installation


**sudo pip3 install seeed-python-dht**

****

Navigate to the 'grove' directory:


**cd grove**

****

Run the test script:
**


**python prueba.py**

****


<a name="_j0w0qkrrgnid"></a>**Connections**

The connections are as follows:

**Grove Sensors:**

- Ultrasonic Sensor connected to port D16
- Buzzer connected to port D24
- Ambient Temperature and Humidity Sensor connected to port D5
- Light Sensor connected to port A0
- Relay connected to port D18


<a name="_q10g10ghms03"></a><a name="_596i51wmm0nk"></a>**Steps to Start the Project Once Everything is Installed**

Version: prueba.py

In my case, I navigate to the grove folder. To do this, I open the terminal and execute the script.

**cd grove**

**python prueba.py**


<a name="_jfaozxm05tfy"></a>**Monitoring**

To monitor, the user simply needs to log in with the credentials provided on ThingSpeak. Once logged in, they can access and view real-time data.

Additionally, this monitoring system allows users to track and analyze various parameters, fostering a comprehensive understanding of the ongoing data trends. Users can receive instant updates and make informed decisions based on the continuously updated information.

<a name="_k4kt4baxzpsj"></a>**Final Reflection**

We have reached the end of the project, and after having completed all its phases, we have realized that we have learned many things about how to work on a Raspberry Pi project.

In addition, the practices carried out during all the weeks have helped us a lot in advancing our project, since before that we had little knowledge about the Raspberry Pi. 

We believe that the project we have carried out meets all the required requirements, we have implemented what we have learned in the best way and the final product can be used in any necessary case today. As for the particular work, both of us have done our part to achieve the final result, the two members have coordinated well, Markel has taken care of the elaboration of the technical part and Jose Javier of the external part (Business model, detect product advantages, etc.)

As for the overall grade of our project, we believe that it could resemble a grade of a high pass or above, taking into account all the grades received previously and seeing how it has turned out in the end. 























<a name="_r7hpsadh5bkd"></a><a name="_kc83l9mzo3w3"></a>**Bibliography**

<https://thingspeak.com/channels/2362056/private_show>

<https://github.com/Seeed-Studio/grove.py>

[https://www.raspberrypi.com/software/ ](https://www.raspberrypi.com/software/)

[Grove Sensors For Raspberry Pi | LinuxAndUbuntu](https://www.linuxandubuntu.com/home/grove-sensors-for-raspberry-pi) 










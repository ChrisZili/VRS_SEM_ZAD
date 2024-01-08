#include "i2c.h"

#define LIDAR_ADD 0x62<<1
uint8_t cmd[1];
uint8_t data[2]={10};

void configuration_set(int configur)      // configuration setting for lidar. it provide different mode of detection
{

	cmd[0] = 0x04;
	HAL_I2C_Mem_Write(&hi2c1,LIDAR_ADD ,0x00,1,cmd,1,0x100);
	switch(configur)
	{
	case 0://default mode , balance mode
		cmd[0]=0x80;
		HAL_I2C_Mem_Write(&hi2c1,LIDAR_ADD ,0x02,1,cmd,1,0x1000);
		cmd[0]=0x04;
		HAL_I2C_Mem_Write(&hi2c1,LIDAR_ADD ,0x04,1,cmd,1,0x1000);
		cmd[0]=0x00;
		HAL_I2C_Mem_Write(&hi2c1,LIDAR_ADD ,0x1c,1,cmd,1,0x1000);
		break;

	case 1://short range, high speed
		cmd[0]=0x1d;
		HAL_I2C_Mem_Write(&hi2c1,LIDAR_ADD ,0x02,1,cmd,1,0x1000);
		cmd[0]=0x08;
		HAL_I2C_Mem_Write(&hi2c1,LIDAR_ADD ,0x04,1,cmd,1,0x1000);
		cmd[0]=0x00;
		HAL_I2C_Mem_Write(&hi2c1,LIDAR_ADD ,0x1c,1,cmd,1,0x1000);
		break;

	case 2://default range, higher speed short range
		cmd[0]=0x80;
		HAL_I2C_Mem_Write(&hi2c1,LIDAR_ADD ,0x02,1,cmd,1,0x1000);
		cmd[0]=0x08;
		HAL_I2C_Mem_Write(&hi2c1,LIDAR_ADD ,0x04,1,cmd,1,0x1000);
		cmd[0]=0x00;
		HAL_I2C_Mem_Write(&hi2c1,LIDAR_ADD ,0x1c,1,cmd,1,0x1000);
		break;


	case 3://maximum Range
		cmd[0]=0xff;
		HAL_I2C_Mem_Write(&hi2c1,LIDAR_ADD ,0x02,1,cmd,1,0x1000);
		cmd[0]=0x08;
		HAL_I2C_Mem_Write(&hi2c1,LIDAR_ADD ,0x04,1,cmd,1,0x1000);
		cmd[0]=0x00;
		HAL_I2C_Mem_Write(&hi2c1,LIDAR_ADD ,0x1c,1,cmd,1,0x1000);
		break;

	case 4://high sensitivity detection, high  measurement
		cmd[0]=0x80;
		HAL_I2C_Mem_Write(&hi2c1,LIDAR_ADD ,0x02,1,cmd,1,0x1000);
		cmd[0]=0x08;
		HAL_I2C_Mem_Write(&hi2c1,LIDAR_ADD ,0x04,1,cmd,1,0x1000);
		cmd[0]=0x80;
		HAL_I2C_Mem_Write(&hi2c1,LIDAR_ADD ,0x1c,1,cmd,1,0x1000);
		break;

	case 5://low sensitivity detection , low  measurement
		cmd[0]=0x80;
		HAL_I2C_Mem_Write(&hi2c1,LIDAR_ADD ,0x02,1,cmd,1,0x1000);
		cmd[0]=0x08;
		HAL_I2C_Mem_Write(&hi2c1,LIDAR_ADD ,0x04,1,cmd,1,0x1000);
		cmd[0]=0xb0;
		HAL_I2C_Mem_Write(&hi2c1,LIDAR_ADD ,0x1c,1,cmd,1,0x1000);
		break;
	}
}

int Get_distance()     // function to get distance
{
	int m_distance=0;
	cmd[0]=0x04;
	HAL_I2C_Mem_Write(&hi2c1,LIDAR_ADD ,0x00,1,cmd,1,100);
	cmd[0]=0x8f;
	HAL_I2C_Master_Transmit(&hi2c1,LIDAR_ADD,cmd,1,100);
	HAL_I2C_Master_Receive(&hi2c1,LIDAR_ADD,data,2,100);
	m_distance = (data[0]<<8)|(data[1]);
	return m_distance ;
}

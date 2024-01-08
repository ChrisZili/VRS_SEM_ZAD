#include "dht11.h"
#include "tim.h"
void HAL_Delay_us(uint32_t nus)
{
//?systic???1us??
//HAL_SYSTICK_Config(HAL_RCC_GetHCLKFreq()/1000000);
////??nus
//HAL_Delay(nus-1);
////??systic???1ms
//HAL_SYSTICK_Config(HAL_RCC_GetHCLKFreq()/1000);
	delayXus(nus);
}

void GPIO_mode_out()
{
	GPIO_InitTypeDef GPIO_InitStruct = {0};

	GPIO_InitStruct.Pin = GPIO_PIN_5;
  GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
  HAL_GPIO_Init(GPIOC, &GPIO_InitStruct);
}

void GPIO_mode_in()
{
	GPIO_InitTypeDef GPIO_InitStruct = {0};

	GPIO_InitStruct.Pin = GPIO_PIN_5;
  GPIO_InitStruct.Mode = GPIO_MODE_INPUT;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  HAL_GPIO_Init(GPIOC, &GPIO_InitStruct);

}


//Reset DHT11
void DHT11_Rst(void)
{
		GPIO_mode_out(); 	//SET OUTPUT
    DHT11_DQ_OUT_OFF; 	//GPIOA.0=0
		//HAL_Delay_us(30);
    HAL_Delay(20);    	//Pull down Least 18ms
    DHT11_DQ_OUT_ON; 	//GPIOA.0=1
		HAL_Delay_us(30);     	//Pull up 20~40us
}

uint8_t DHT11_Check(void)
{
	uint8_t retry=0;
	GPIO_mode_in();//SET INPUT
    while (DHT11_DQ_IN&&retry<100)//DHT11 Pull down 40~80us
	{
		retry++;
		HAL_Delay_us(1);
	};
	if(retry>=100)
		return 1;
	else
		retry=0;
    while (!DHT11_DQ_IN&&retry<100)//DHT11 Pull up 40~80us
	{
		retry++;
		HAL_Delay_us(1);
	};
	if(retry>=100)
		return 1;//chack error
	return 0;
}

uint8_t DHT11_Read_Bit(void)
{
 	uint8_t retry=0;
	while(DHT11_DQ_IN&&retry<100)//wait become Low level
	{
		retry++;
		HAL_Delay_us(1);
	}
	retry=0;
	while(!DHT11_DQ_IN&&retry<100)//wait become High level
	{
		retry++;
		HAL_Delay_us(1);
	}
	HAL_Delay_us(40);//wait 40us
	if(DHT11_DQ_IN)
		return 1;
	else
		return 0;
}

uint8_t DHT11_Read_Byte(void)
{
    uint8_t i,dat;
    dat=0;
	for (i=0;i<8;i++)
	{
   		dat<<=1;
	    dat|=DHT11_Read_Bit();
    }
    return dat;
}

uint8_t DHT11_Read_Data(uint8_t *temperature,uint8_t *humidity)
{
 	uint8_t buf[5];
	uint8_t i;
	DHT11_Rst();
	if(DHT11_Check()==0)
	{
		for(i=0;i<5;i++)
		{
			buf[i]=DHT11_Read_Byte();
		}
		if((buf[0]+buf[1]+buf[2]+buf[3])==buf[4])
		{
			*humidity=buf[0];
			*temperature=buf[2];
		}
	}
	else
		return 1;
	return 0;
}




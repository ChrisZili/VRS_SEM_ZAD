#ifndef __DHT11_H
#define __DHT11_H

#ifdef __cplusplus
extern "C" {
#endif


#include "main.h"

//Set GPIO Direction
//#define DHT11_IO_IN  {GPIOA->MODER&0XFFFFFFFC;GPIOA->PUPDR&0XFFFFFFFC;GPIOA->PUPDR|0XFFFFFFFD}	//PA0
//#define DHT11_IO_OUT {GPIOA->MODER&0XFFFFFFFC;GPIOA->MODER&0XFFFFFFFD;GPIOA->OTYPER&0XFFFFFFFD;GPIOA->OSPEEDR&0XFFFFFFFC;GPIOA->PUPDR&0XFFFFFFFC;GPIOA->PUPDR|0XFFFFFFFD}	//PA0

#define	DHT11_DQ_OUT_OFF   	HAL_GPIO_WritePin( GPIOC , GPIO_PIN_5, GPIO_PIN_RESET)
#define	DHT11_DQ_OUT_ON   	HAL_GPIO_WritePin(GPIOC , GPIO_PIN_5 , GPIO_PIN_SET)
#define	DHT11_DQ_IN  		HAL_GPIO_ReadPin( GPIOC , GPIO_PIN_5 )



void HAL_Delay_us(uint32_t nus);
uint8_t DHT11_Init(void); //Init DHT11
uint8_t DHT11_Read_Data(uint8_t *temperature,uint8_t *humidity); //Read DHT11 Value
uint8_t DHT11_Read_Byte(void);//Read One Byte
uint8_t DHT11_Read_Bit(void);//Read One Bit
uint8_t DHT11_Check(void);//Chack DHT11
void DHT11_Rst(void);//Reset DHT11



#ifdef __cplusplus
}
#endif
#endif /*__ GPIO_H__ */











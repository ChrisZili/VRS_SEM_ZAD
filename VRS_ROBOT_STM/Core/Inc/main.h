/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file           : main.h
  * @brief          : Header for main.c file.
  *                   This file contains the common defines of the application.
  ******************************************************************************
  * @attention
  *
  * Copyright (c) 2024 STMicroelectronics.
  * All rights reserved.
  *
  * This software is licensed under terms that can be found in the LICENSE file
  * in the root directory of this software component.
  * If no LICENSE file comes with this software, it is provided AS-IS.
  *
  ******************************************************************************
  */
/* USER CODE END Header */

/* Define to prevent recursive inclusion -------------------------------------*/
#ifndef __MAIN_H
#define __MAIN_H

#ifdef __cplusplus
extern "C" {
#endif

/* Includes ------------------------------------------------------------------*/
#include "stm32f4xx_hal.h"

/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */

/* USER CODE END Includes */

/* Exported types ------------------------------------------------------------*/
/* USER CODE BEGIN ET */

/* USER CODE END ET */

/* Exported constants --------------------------------------------------------*/
/* USER CODE BEGIN EC */

/* USER CODE END EC */

/* Exported macro ------------------------------------------------------------*/
/* USER CODE BEGIN EM */

/* USER CODE END EM */

/* Exported functions prototypes ---------------------------------------------*/
void Error_Handler(void);

/* USER CODE BEGIN EFP */
void parseStringAndStore(uint8_t *str, uint8_t size);
void hard_stop();
void set_motors();
int Get_distance();
void setCamera();
void configuration_set(int configur);
int mapValue(int input);
float Measure_Distance(void);
/* USER CODE END EFP */

/* Private defines -----------------------------------------------------------*/
#define B1_Pin GPIO_PIN_13
#define B1_GPIO_Port GPIOC
#define CAM_PWM_Y_Pin GPIO_PIN_1
#define CAM_PWM_Y_GPIO_Port GPIOA
#define USART_TX_Pin GPIO_PIN_2
#define USART_TX_GPIO_Port GPIOA
#define USART_RX_Pin GPIO_PIN_3
#define USART_RX_GPIO_Port GPIOA
#define CAM_PWM_X_Pin GPIO_PIN_5
#define CAM_PWM_X_GPIO_Port GPIOA
#define DIR1_Pin GPIO_PIN_7
#define DIR1_GPIO_Port GPIOC
#define ECHO_Pin GPIO_PIN_9
#define ECHO_GPIO_Port GPIOC
#define TRIG_Pin GPIO_PIN_8
#define TRIG_GPIO_Port GPIOA
#define TMS_Pin GPIO_PIN_13
#define TMS_GPIO_Port GPIOA
#define TCK_Pin GPIO_PIN_14
#define TCK_GPIO_Port GPIOA
#define SWO_Pin GPIO_PIN_3
#define SWO_GPIO_Port GPIOB
#define DIR2_Pin GPIO_PIN_6
#define DIR2_GPIO_Port GPIOB

/* USER CODE BEGIN Private defines */
extern uint8_t buffer[13];
typedef struct
{
uint16_t L_PWM;
uint16_t R_PWM;
uint8_t L_DIR;
uint8_t R_DIR;
} PWM_Control_TypeDef;
typedef struct
{
	uint16_t X_PWM;
	uint16_t Y_PWM;
	uint8_t X_DIR;
	uint8_t Y_DIR;
	uint8_t X_RELATIVE;
	uint8_t Y_RELATIVE;
	int X_POS;
	int Y_POS;
} Camera_Control_Typedef;

/* USER CODE END Private defines */

#ifdef __cplusplus
}
#endif

#endif /* __MAIN_H */

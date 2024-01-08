/* USER CODE BEGIN Header */
/**
 ******************************************************************************
 * @file           : main.c
 * @brief          : Main program body
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
/* Includes ------------------------------------------------------------------*/
#include "main.h"
#include "dma.h"
#include "i2c.h"
#include "tim.h"
#include "usart.h"
#include "gpio.h"

/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */
#include "string.h"
#include "stdio.h"
#include "configParams.h"
#include "DHT11.h"
/* USER CODE END Includes */

/* Private typedef -----------------------------------------------------------*/
/* USER CODE BEGIN PTD */
#define LIDAR_ADD 0x62<<1										// i2c slave address of lidar lite

uint32_t m_distance, object_distance; // define the variable to get distance value

char str[100];
/* USER CODE END PTD */

/* Private define ------------------------------------------------------------*/
/* USER CODE BEGIN PD */

/* USER CODE END PD */

/* Private macro -------------------------------------------------------------*/
/* USER CODE BEGIN PM */

/* USER CODE END PM */

/* Private variables ---------------------------------------------------------*/

/* USER CODE BEGIN PV */
uint8_t buffer[13];
uint8_t bufferOut[13];
float rear_sensor = 0;

uint8_t temperature;
uint8_t humidity;

uint32_t pMillis;
uint32_t val1 = 0;
uint32_t val2 = 0;
uint16_t distance  = 0;


PWM_Control_TypeDef PWM_Control = { .L_PWM = 0, .R_PWM = 0, .L_DIR = 0, .R_DIR =0 };

Camera_Control_Typedef Camera_Control = { .X_PWM = 50, .Y_PWM = 50, .X_DIR =0, .Y_DIR = 0, .X_RELATIVE = 0, .Y_RELATIVE= 0, .X_POS = 0, .Y_POS = 0};
/* USER CODE END PV */

/* Private function prototypes -----------------------------------------------*/
void SystemClock_Config(void);
/* USER CODE BEGIN PFP */
/* USER CODE END PFP */

/* Private user code ---------------------------------------------------------*/
/* USER CODE BEGIN 0 */

/* USER CODE END 0 */

/**
  * @brief  The application entry point.
  * @retval int
  */
int main(void)
{
  /* USER CODE BEGIN 1 */

  /* USER CODE END 1 */

  /* MCU Configuration--------------------------------------------------------*/

  /* Reset of all peripherals, Initializes the Flash interface and the Systick. */
  HAL_Init();

  /* USER CODE BEGIN Init */

  /* USER CODE END Init */

  /* Configure the system clock */
  SystemClock_Config();

  /* USER CODE BEGIN SysInit */

  /* USER CODE END SysInit */

  /* Initialize all configured peripherals */
  MX_GPIO_Init();
  MX_DMA_Init();
  MX_TIM2_Init();
  MX_USART2_UART_Init();
  MX_TIM11_Init();
  MX_I2C1_Init();
  MX_TIM3_Init();
  MX_USART1_UART_Init();
  MX_TIM10_Init();
  MX_TIM1_Init();
  MX_USART6_UART_Init();
  /* USER CODE BEGIN 2 */
  HAL_TIM_Base_Start(&htim1);
  HAL_GPIO_WritePin(TRIG_GPIO_Port, TRIG_Pin, GPIO_PIN_RESET);

	HAL_TIM_PWM_Start(&htim2, TIM_CHANNEL_2);
	HAL_TIM_PWM_Start(&htim2, TIM_CHANNEL_1);
	HAL_TIM_PWM_Start(&htim3, TIM_CHANNEL_1);
	HAL_TIM_PWM_Start(&htim3, TIM_CHANNEL_2);

	HAL_TIM_Base_Start_IT(&htim11);
	configuration_set(4);

	setCamera();

	int timerTick = 0;
	int speed = 0;
	int max_Speed = 0;
	int speed_signal = 0;
	int dir_signal = 0;

	if (HAL_UART_Receive_DMA(&huart1, buffer, 13) != HAL_OK)
		Error_Handler();
	if (HAL_UART_Receive_DMA(&huart2, buffer, 13) != HAL_OK)
		Error_Handler();

  /* USER CODE END 2 */

  /* Infinite loop */
  /* USER CODE BEGIN WHILE */
	while (1) {

		set_motors();





		if(__HAL_TIM_GET_COUNTER(&htim11) > 65000){
			timerTick++;
			__HAL_TIM_SetCounter(&htim11,0);

			if(timerTick %70 == 0 ){
				setCamera();
			}
			if(timerTick == 625){

			object_distance = Get_distance();
			sprintf(bufferOut, "L%d", object_distance);
			bufferOut[12] = '\n';
			HAL_UART_Transmit(&huart1, bufferOut, sizeof(bufferOut),HAL_MAX_DELAY);
			HAL_UART_Transmit(&huart2, bufferOut, sizeof(bufferOut),HAL_MAX_DELAY);

			DHT11_Read_Data(&temperature,&humidity);
			sprintf(bufferOut, "T%d", temperature);
			bufferOut[12] = '\n';
			HAL_UART_Transmit(&huart1, bufferOut, sizeof(bufferOut),HAL_MAX_DELAY);
			HAL_UART_Transmit(&huart2, bufferOut, sizeof(bufferOut),HAL_MAX_DELAY);

			sprintf(bufferOut, "H%d", humidity);
			bufferOut[12] = '\n';
			HAL_UART_Transmit(&huart1, bufferOut, sizeof(bufferOut),HAL_MAX_DELAY);
			HAL_UART_Transmit(&huart2, bufferOut, sizeof(bufferOut),HAL_MAX_DELAY);

			rear_sensor = Measure_Distance();
			sprintf(bufferOut, "R%.2f", rear_sensor);
			bufferOut[12] = '\n';
			HAL_UART_Transmit(&huart1, bufferOut, sizeof(bufferOut),HAL_MAX_DELAY);
			HAL_UART_Transmit(&huart2, bufferOut, sizeof(bufferOut),HAL_MAX_DELAY);
		timerTick = 0;
		}
		}
    /* USER CODE END WHILE */

    /* USER CODE BEGIN 3 */
	}
  /* USER CODE END 3 */
}

/**
  * @brief System Clock Configuration
  * @retval None
  */
void SystemClock_Config(void)
{
  RCC_OscInitTypeDef RCC_OscInitStruct = {0};
  RCC_ClkInitTypeDef RCC_ClkInitStruct = {0};

  /** Configure the main internal regulator output voltage
  */
  __HAL_RCC_PWR_CLK_ENABLE();
  __HAL_PWR_VOLTAGESCALING_CONFIG(PWR_REGULATOR_VOLTAGE_SCALE2);

  /** Initializes the RCC Oscillators according to the specified parameters
  * in the RCC_OscInitTypeDef structure.
  */
  RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_HSI;
  RCC_OscInitStruct.HSIState = RCC_HSI_ON;
  RCC_OscInitStruct.HSICalibrationValue = RCC_HSICALIBRATION_DEFAULT;
  RCC_OscInitStruct.PLL.PLLState = RCC_PLL_ON;
  RCC_OscInitStruct.PLL.PLLSource = RCC_PLLSOURCE_HSI;
  RCC_OscInitStruct.PLL.PLLM = 16;
  RCC_OscInitStruct.PLL.PLLN = 336;
  RCC_OscInitStruct.PLL.PLLP = RCC_PLLP_DIV4;
  RCC_OscInitStruct.PLL.PLLQ = 7;
  if (HAL_RCC_OscConfig(&RCC_OscInitStruct) != HAL_OK)
  {
    Error_Handler();
  }

  /** Initializes the CPU, AHB and APB buses clocks
  */
  RCC_ClkInitStruct.ClockType = RCC_CLOCKTYPE_HCLK|RCC_CLOCKTYPE_SYSCLK
                              |RCC_CLOCKTYPE_PCLK1|RCC_CLOCKTYPE_PCLK2;
  RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_PLLCLK;
  RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1;
  RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV2;
  RCC_ClkInitStruct.APB2CLKDivider = RCC_HCLK_DIV1;

  if (HAL_RCC_ClockConfig(&RCC_ClkInitStruct, FLASH_LATENCY_2) != HAL_OK)
  {
    Error_Handler();
  }
}

/* USER CODE BEGIN 4 */
void parseStringAndStore(uint8_t *str, uint8_t size) {
	uint16_t temp = 0;
	if (str[0] == '1') {
		for (uint8_t i = 1; i < size; i++) {
			if (str[i] == 'R') {
				if (str[i + 1] == '+')
					PWM_Control.R_DIR = 0;
				else if (str[i + 1] == '-')
					PWM_Control.R_DIR = 1;
				temp = (str[i + 2] - '0') * 100;
				temp += (str[i + 3] - '0') * 10;
				temp += (str[i + 4] - '0');
				temp *= 10;
				if (temp <= 1000 && temp > 0)
					PWM_Control.R_PWM = temp - 1;
				else
					PWM_Control.R_PWM = 0;

				temp = 0;
			}
			if (str[i] == 'L') {
				if (str[i + 1] == '+')
					PWM_Control.L_DIR = 0;
				else if (str[i + 1] == '-')
					PWM_Control.L_DIR = 1;
				temp = (str[i + 2] - '0') * 100;
				temp += (str[i + 3] - '0') * 10;
				temp += (str[i + 4] - '0');
				temp *= 10;
				if (temp <= 1000 && temp > 0)
					PWM_Control.L_PWM = temp - 1;
				else
					PWM_Control.L_PWM = 0;
			}
		}
	} else if (str[0] == '2') {

		for (uint8_t i = 1; i < size; i++) {
			if (str[i] == 'X') {
				if (str[i + 1] == '+')
					Camera_Control.X_DIR = 1;
				else if (str[i + 1] == '-')
					Camera_Control.X_DIR = 0;
				temp = (str[i + 2] - '0') * 100;
				temp += (str[i + 3] - '0') * 10;
				temp += (str[i + 4] - '0');
//				temp/=25;
				if (temp <= 10000 && temp > 0)
					Camera_Control.X_RELATIVE = temp - 1;
				else
					Camera_Control.X_RELATIVE = 0;

				temp = 0;
			}
			if (str[i] == 'Y') {
				if (str[i + 1] == '+')
					Camera_Control.Y_DIR = 1;
				else if (str[i + 1] == '-')
					Camera_Control.Y_DIR = 0;
				temp = (str[i + 2] - '0') * 100;
				temp += (str[i + 3] - '0') * 10;
				temp += (str[i + 4] - '0');
//				temp/=25;
				if (temp <= 10000 && temp > 0)
					Camera_Control.Y_RELATIVE = temp - 1;
				else
					Camera_Control.Y_RELATIVE = 0;
			}

		}

	}
	else if(str[0] == '3') {

		sprintf(bufferOut, "%d", object_distance);
		bufferOut[12] = '\n';
		HAL_UART_Transmit(&huart1, bufferOut, sizeof(bufferOut),HAL_MAX_DELAY);
		HAL_UART_Transmit(&huart2, bufferOut, sizeof(bufferOut),HAL_MAX_DELAY);
	}
	else if(str[0] =='4'){}

}

void set_motors() {

	HAL_GPIO_WritePin(DIR1_GPIO_Port, DIR1_Pin, PWM_Control.R_DIR);
	HAL_GPIO_WritePin(DIR2_GPIO_Port, DIR2_Pin, PWM_Control.L_DIR);

	if(PWM_Control.R_PWM >DEADZONE_MOTORS)__HAL_TIM_SET_COMPARE(&htim3, TIM_CHANNEL_1, PWM_Control.R_PWM);
	else __HAL_TIM_SET_COMPARE(&htim3, TIM_CHANNEL_1, 0);
	if(PWM_Control.L_PWM > DEADZONE_MOTORS)	__HAL_TIM_SET_COMPARE(&htim3, TIM_CHANNEL_2, PWM_Control.L_PWM);
	else 	__HAL_TIM_SET_COMPARE(&htim3, TIM_CHANNEL_2, 0);
}
void hard_stop() {
//	__HAL_TIM_SET_COMPARE(&htim1, TIM_CHANNEL_1, 0);
//	__HAL_TIM_SET_COMPARE(&htim1, TIM_CHANNEL_2, 0);
//	PWM_Control.L_PWM = 0;
//	PWM_Control.R_PWM = 0;
}
void setCamera() {

	if(Camera_Control.X_DIR == 1 && Camera_Control.X_PWM < 80)__HAL_TIM_SET_COMPARE(&htim2, TIM_CHANNEL_1, Camera_Control.X_PWM += Camera_Control.X_RELATIVE);
	if(Camera_Control.X_DIR == 0 && Camera_Control.X_PWM > 20)__HAL_TIM_SET_COMPARE(&htim2, TIM_CHANNEL_1, Camera_Control.X_PWM -= Camera_Control.X_RELATIVE);

	if(Camera_Control.Y_DIR == 1 && Camera_Control.Y_PWM <80)__HAL_TIM_SET_COMPARE(&htim2, TIM_CHANNEL_2, Camera_Control.Y_PWM += Camera_Control.Y_RELATIVE );
	if(Camera_Control.Y_DIR == 0 && Camera_Control.Y_PWM > 20)__HAL_TIM_SET_COMPARE(&htim2, TIM_CHANNEL_2, Camera_Control.Y_PWM -= Camera_Control.Y_RELATIVE );
}
float Measure_Distance(void) {
	;
    // Send trigger pulse (10 us) on PA8
	  HAL_GPIO_WritePin(TRIG_GPIO_Port, TRIG_Pin, GPIO_PIN_SET);
	  __HAL_TIM_SET_COUNTER(&htim1, 0);
	   while (__HAL_TIM_GET_COUNTER (&htim1) < 10);  // wait for 10 us
	   HAL_GPIO_WritePin(TRIG_GPIO_Port, TRIG_Pin, GPIO_PIN_RESET);

	   pMillis = HAL_GetTick();
	   while (!(HAL_GPIO_ReadPin (ECHO_GPIO_Port, ECHO_Pin)) && pMillis + 10 >  HAL_GetTick());
	   val1 = __HAL_TIM_GET_COUNTER (&htim1);

	   pMillis = HAL_GetTick();
	   while ((HAL_GPIO_ReadPin (ECHO_GPIO_Port, ECHO_Pin)) && pMillis + 50 > HAL_GetTick());
	   val2 = __HAL_TIM_GET_COUNTER (&htim1);

	   distance = (val2-val1)* 0.034/2;

    return distance;
}


/* USER CODE END 4 */

/**
  * @brief  This function is executed in case of error occurrence.
  * @retval None
  */
void Error_Handler(void)
{
  /* USER CODE BEGIN Error_Handler_Debug */
	/* User can add his own implementation to report the HAL error return state */
	__disable_irq();
	while (1) {
	}
  /* USER CODE END Error_Handler_Debug */
}

#ifdef  USE_FULL_ASSERT
/**
  * @brief  Reports the name of the source file and the source line number
  *         where the assert_param error has occurred.
  * @param  file: pointer to the source file name
  * @param  line: assert_param error line source number
  * @retval None
  */
void assert_failed(uint8_t *file, uint32_t line)
{
  /* USER CODE BEGIN 6 */
  /* User can add his own implementation to report the file name and line number,
     ex: printf("Wrong parameters value: file %s on line %d\r\n", file, line) */
  /* USER CODE END 6 */
}
#endif /* USE_FULL_ASSERT */

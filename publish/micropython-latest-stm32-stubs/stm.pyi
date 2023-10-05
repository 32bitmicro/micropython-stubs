"""
Functionality specific to STM32 MCUs.

MicroPython module: https://docs.micropython.org/en/latest/library/stm.html

This module provides functionality specific to STM32 microcontrollers, including
direct access to peripheral registers.
"""
from typing import Tuple, Any
from _typeshed import Incomplete

SPI_I2SPR: int
RTC_DR: int
RTC_CR: int
RTC_CALR: int
RTC_ISR: int
RTC_SSR: int
RTC_SHIFTR: int
RTC_PRER: int
RTC_CALIBR: int
RTC_BKP5R: int
RTC_BKP4R: int
RTC_BKP3R: int
RTC_BKP6R: int
RTC_BKP9R: int
RTC_BKP8R: int
RTC_BKP7R: int
RTC_TAFCR: int
SPI_CR1: int
SPI3: int
SPI2: int
SPI_CR2: int
SPI_I2SCFGR: int
SPI_DR: int
SPI_CRCPR: int
SPI1: int
RTC_TSSSR: int
RTC_TSDR: int
RTC_TR: int
RTC_TSTR: int
SDIO: int
RTC_WUTR: int
RTC_WPR: int
RTC_BKP2R: int
RNG: int
RCC_SSCGR: int
RCC_PLLI2SCFGR: int
RNG_CR: int
RTC: int
RNG_SR: int
RNG_DR: int
RCC_PLLCFGR: int
RCC_BDCR: int
RCC_APB2RSTR: int
RCC_APB2LPENR: int
RCC_CFGR: int
RCC_CSR: int
RCC_CR: int
RCC_CIR: int
RTC_ALRMAR: int
RTC_BKP16R: int
RTC_BKP15R: int
RTC_BKP14R: int
RTC_BKP17R: int
RTC_BKP1R: int
RTC_BKP19R: int
RTC_BKP18R: int
RTC_BKP13R: int
RTC_ALRMBSSR: int
RTC_ALRMBR: int
RTC_ALRMASSR: int
RTC_BKP0R: int
RTC_BKP12R: int
RTC_BKP11R: int
RTC_BKP10R: int
WWDG_SR: int
SPI_RXCRCR: int
TIM_RCR: int
TIM_PSC: int
TIM_OR: int
TIM_SMCR: int
UART5: int
UART4: int
TIM_SR: int
TIM_EGR: int
TIM_CR1: int
TIM_CNT: int
TIM_CCR4: int
TIM_CR2: int
TIM_DMAR: int
TIM_DIER: int
TIM_DCR: int
USART1: int
USB_OTG_FS: int
USART_SR: int
USART_GTPR: int
USB_OTG_HS: int
WWDG_CR: int
WWDG_CFR: int
WWDG: int
USART_DR: int
USART6: int
USART3: int
USART2: int
USART_BRR: int
USART_CR3: int
USART_CR2: int
USART_CR1: int
TIM_CCR3: int
TIM1: int
SYSCFG_PMC: int
SYSCFG_MEMRMP: int
TIM10: int
TIM13: int
TIM12: int
TIM11: int
SYSCFG_EXTICR3: int
SYSCFG: int
SPI_TXCRCR: int
SPI_SR: int
SYSCFG_CMPCR: int
SYSCFG_EXTICR2: int
SYSCFG_EXTICR1: int
SYSCFG_EXTICR0: int
TIM14: int
TIM_CCER: int
TIM_BDTR: int
TIM_ARR: int
TIM_CCMR1: int
TIM_CCR2: int
TIM_CCR1: int
TIM_CCMR2: int
TIM9: int
TIM4: int
TIM3: int
TIM2: int
TIM5: int
TIM8: int
TIM7: int
TIM6: int
EXTI_SWIER: int
DAC_DOR1: int
DAC_DHR8RD: int
DAC_DHR8R2: int
DAC_DOR2: int
DBGMCU: int
DAC_SWTRIGR: int
DAC_SR: int
DAC_DHR8R1: int
DAC_DHR12L2: int
DAC_DHR12L1: int
DAC_CR: int
DAC_DHR12LD: int
DAC_DHR12RD: int
DAC_DHR12R2: int
DAC_DHR12R1: int
DBGMCU_APB1FZ: int
EXTI_EMR: int
EXTI: int
DMA_LISR: int
EXTI_FTSR: int
EXTI_RTSR: int
EXTI_PR: int
EXTI_IMR: int
DMA_LIFCR: int
DBGMCU_IDCODE: int
DBGMCU_CR: int
DBGMCU_APB2FZ: int
DMA1: int
DMA_HISR: int
DMA_HIFCR: int
DMA2: int
DAC1: int
ADC_JDR3: int
ADC_JDR2: int
ADC_JDR1: int
ADC_JDR4: int
ADC_JOFR3: int
ADC_JOFR2: int
ADC_JOFR1: int
ADC_HTR: int
ADC2: int
ADC123_COMMON: int
ADC1: int
ADC3: int
ADC_DR: int
ADC_CR2: int
ADC_CR1: int
ADC_JOFR4: int
CRC: int
CAN2: int
CAN1: int
CRC_CR: int
DAC: int
CRC_IDR: int
CRC_DR: int
ADC_SR: int
ADC_SMPR1: int
ADC_LTR: int
ADC_JSQR: int
ADC_SMPR2: int
ADC_SQR3: int
ADC_SQR2: int
ADC_SQR1: int
RCC_APB2ENR: int
FLASH: int
IWDG: int
I2S3EXT: int
I2S2EXT: int
IWDG_KR: int
IWDG_SR: int
IWDG_RLR: int
IWDG_PR: int
I2C_TRISE: int
I2C_DR: int
I2C_CR2: int
I2C_CR1: int
I2C_OAR1: int
I2C_SR2: int
I2C_SR1: int
I2C_OAR2: int
PWR: int
RCC_AHB3LPENR: int
RCC_AHB3ENR: int
RCC_AHB2RSTR: int
RCC_AHB3RSTR: int
RCC_APB1RSTR: int
RCC_APB1LPENR: int
RCC_APB1ENR: int
RCC_AHB2LPENR: int
RCC: int
PWR_CSR: int
PWR_CR: int
RCC_AHB1ENR: int
RCC_AHB2ENR: int
RCC_AHB1RSTR: int
RCC_AHB1LPENR: int
I2C_CCR: int
GPIOD: int
GPIOC: int
GPIOB: int
GPIOE: int
GPIOH: int
GPIOG: int
GPIOF: int
GPIOA: int
FLASH_KEYR: int
FLASH_CR: int
FLASH_ACR: int
FLASH_OPTCR: int
FLASH_SR: int
FLASH_OPTKEYR: int
FLASH_OPTCR1: int
GPIOI: int
GPIO_OTYPER: int
GPIO_OSPEEDR: int
GPIO_ODR: int
GPIO_PUPDR: int
I2C3: int
I2C2: int
I2C1: int
GPIO_MODER: int
GPIO_BSRR: int
GPIO_AFR1: int
GPIO_AFR0: int
GPIO_BSRRH: int
GPIO_LCKR: int
GPIO_IDR: int
GPIO_BSRRL: int
mem32: Any
mem8: Any
mem16: Any

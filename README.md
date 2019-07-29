## Weather Mini Challenge
Suppose you live in Ribeirão Preto. Should you take an umbrella?

You tell us!

If the air humidity on a given day is **greater** than **70%**, it is a good idea to take an umbrella with you.
Your goal is to fetch the Ribeirão Preto air humidity forecast for the next **seven** days from https://openweathermap.org/api and display the following message template:

*You should take an umbrella in these days: ....*

For instance, if on the next seven days air humidity will be greater than 70% on Monday, Tuesday and Wednesday, you must display the message:

*You should take an umbrella in these days: Monday, Tuesday and Wednesday.*

 -------------------------------------------------------------------------------

Felipe Almeida Comments:

In the https://openweathermap.org/api there's no free API to return the forecast for seven days, however it's possible to retrieve five days with an interval of three hours.

So what I've done is getting to know the hours of that five days that trigger the condition and the response is aggregated by the weekday name.

Another observation is that you should modify the API Key with your own for the script to run.

-------------------------------------------------------------------------------

// Package weather provides tools to obtain the forecast.
package weather

var (
	// CurrentCondition is string of the current condition os weather.
	CurrentCondition string
    // CurrentLocation is a string of the location of the forecast.
	CurrentLocation  string
)

// Forecast takes two values to return a description of weather.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}

# Testing

Once the portal was operational I set about testing it for errors and to ensure any possible errors that can be made were caught.

The deployed project live link is [HERE](https://expenses--calculator-4db02840ab2a.herokuapp.com/)

The following tests were carried out to ensure the portal is working correctly

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Name and Last name input | User is asked to enter their name | First & Last name input| Works as expected | 
| Name input | User inputs symbol or number | Error message appears | Works as expected | 
| Job Position | User selects their Job Position | User selects a - e | Works as expected | 
| Job Position | User selects invalid letter | Error message appears then loops back to question | Works as expected | 
| Expenses | User is asked about thier expenses| Information confirmed as true | Works as expected |
| Expenses | Expenses entered incorrect |Error message appears then loops back to question | Works as expected |
| Confirm Expenses | If user selects n  | then loops back to expenses question again | Works as expected |
| Confirm Expenses | If user selects y  | then updates data to google sheets | Works as expected |

## Testing Browsers
The portal was tested in the following browsers (based on my own testing and those of people who tested the portal):

- Chrome
- Firefox
- Edge

It worked without issues in the above browsers.

### Validation

For validation I user [snyk](snyk.io) to check for any errors in my code.

* [run.py Validation](snyk.io) - Pass

---

### [Back to README.md](README.md)
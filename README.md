# URBAN BOULEVARD EVENT SPACE BOOKER
Urban Boulevard is a concise, straightforward booking system allowing for users looking for event spaces for hosting of events and activities to browse the range of spaces included and with a simple few clicks, successfully enabling the reservation of a specific venue at the desired date and time.
## CORE FUNCTIONALITIES
### LOGIN PAGE
![image](https://github.com/wzngekj/EventSpaceBooker/assets/147592707/f2db5a7a-a0c5-491a-a9ae-ac3eb3e1ab7c)
![image](https://github.com/wzngekj/EventSpaceBooker/assets/147592707/532f6c95-5bb1-4a79-87b5-42bf664314dd)
- On loading of the flask application, users are routed to `"/"` where `login.html` is loaded
- Offers the basic functionalities of a login page, inclusive of signing in with the user's distinct email and his password
  * A key feature implemented is the toggling of the eye icon switching from eye-no-slash and eye-slash allowing the user to conceal and reveal the password
- Upon submitting the form, 2 kinds of backend verification are conducted by querying using SQL on the credentials table in `credentials.db`
  * To check for valid email, if no valid email is found, the system redirects the user to `relogin.html` where the page prompts the user to re-enter the password and username, displaying an incorrect password or username message
  * After a valid email is found, the system further checks if the password registered and associated with the matches with the password input, if not `relogin.html` is rendered
- Upon successful authentication, the user is redirected to `"/area"`
- If the user is new and wishes to register, a click on the `Register Now` will bring the user to the register page from `register.html` by the re-routing to `\register`
### RELOGIN PAGE
![image](https://github.com/wzngekj/EventSpaceBooker/assets/147592707/56ae2f2e-bc9e-4a57-b8f0-b38bb34adc8f)
### REGISTER PAGE
![image](https://github.com/wzngekj/EventSpaceBooker/assets/147592707/9663236a-ccac-4cef-a3c8-592e6fd9e6cf)
![image](https://github.com/wzngekj/EventSpaceBooker/assets/147592707/4a5103f1-651b-40b7-9de0-dd7e937ec7f0)
![image](https://github.com/wzngekj/EventSpaceBooker/assets/147592707/b0fc97b7-1857-4629-8970-30736aca261b)
![image](https://github.com/wzngekj/EventSpaceBooker/assets/147592707/121d22e4-ba4c-48b6-b839-6cd75542734a)
- Users are routed to the register page by `"\register"`
- Mandates the fundamentals of a register page, including the name, email, password and re-enter password fields
- There are multiple key features starting with the red bolded `INVALID EMAIL!` and `WEAK PASSWORD!` message, and the disabled button to prevent unsuccessful registration. The disabled register button will be enabled when the below conditions are met
  * `Condition 1`: Javascript used to verify if the name field has NULL input. Upon valid input, the boolean condition1 is true
  * `Condition 2`: Javascript and RegEx is used to verify if the email input ends with a specific pattern ` pattern = ".+@.+\.com"`. Upon valid pattern, condition 2 is true and additionally, the `INVALID EMAIL!` will disappear
  * `Condition 3`: Javascript is used to verify whether the password entered is strong enough, in which in the software, is determined by the length. Once the password is longer than 8 characters, the `WEAK PASSWORD!` will disappear and this condition is now true.
  * `Condition 4`: Lastly, javascript is used to verify whether the 2 password field matches, if valid the last condition is true and the register button is enabled. At the top has demonstrated a few cases of the register button activation
- Once registered, the program re-routes you back to `"\login"` and prompts you to log in with the user's new credentials




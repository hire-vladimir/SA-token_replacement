# As of Splunk Enterprise Security 5.0 and greater, this app has been deprecated in favor of native **expandtoken** command that ships with the product.

## *expandtoken* usage

For targeted fields:
```
 | localop | stats count

 | eval rule_title="hello $name$", rule_description="this means $name$, is $value$"
 | eval name="vladimir", value="awesome"

 | expandtoken rule_title rule_description
```

For any field:
```
 | localop | stats count

 | eval rule_title="hello $name$", rule_description="this means $name$, is $value$"
 | eval name="vladimir", value="awesome"

 | expandtoken
```


---
# Into
Allows $token$ replacement with field values

# Disclaimer
Command should be treated as prototype/example. Has not been fully tested, no logging exists.

# Usage
```
 | localop | stats count

 | eval rule_title="hello $name$", rule_description="this means $name$, is $value$"
 | eval name="vladimir", value="awesome"

 | replacetokens fields="rule_title,rule_description"
```

OR

```
index="notable"

| lookup update=true correlationsearches_lookup _key as source OUTPUTNEW security_domain, severity, rule_name, description as savedsearch_description, rule_title, rule_description, drilldown_name, drilldown_search, drilldown_earliest_offset, drilldown_latest_offset, default_status, default_owner, next_steps, recommended_actions

| replacetokens fields="rule_title,rule_description"
```

# Screenshot
![SA-token_replacement_overview](https://raw.githubusercontent.com/hire-vladimir/SA-token_replacement/master/static/screenshot.png)

# Legal
* *Splunk* is a registered trademark of Splunk, Inc.

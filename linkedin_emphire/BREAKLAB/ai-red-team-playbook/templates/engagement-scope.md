# Engagement scope and rules of engagement

Copy this file per engagement. Nothing is tested until the stop condition has a name and a number.

## Parties

| | |
|---|---|
| Client | |
| System under test | |
| Environment | production / staging / clone |
| Tester | |
| Client contact for test questions | |
| Person who can invoke the stop | |
| Their number, reachable out of hours | |

## Authorised targets

Name each one. A domain, an application, a model endpoint, a tool. Anything not listed is out of scope.

| Target | Address or identifier | Notes |
|---|---|---|
| | | |

## Out of scope, explicitly

- Live third party services and their data
- Real customer records
- Destructive writes, including updates that a user would not be able to reverse
- Denial of service against shared infrastructure
- Model training or fine tuning
- Social engineering of staff
- Physical access

## Permitted actions

State the loudest thing you may do, so that nothing below it is in doubt.

- Authentication: normal user accounts, supplied by the client
- Volume: up to N requests per minute per target
- Data: synthetic records only

## Stop condition

Testing halts immediately if any of the following occurs, and the named person above is contacted before anything else happens:

- A finding affects a real customer or a live third party
- An action triggers an unintended write
- A production metric moves outside its expected band

## Data handling

| | |
|---|---|
| What will be copied | |
| Where it is stored | |
| Who can see findings before the client | |
| Deletion date | |

## Disclosure

| | |
|---|---|
| Channel for findings | |
| Timeline for the client to respond | |
| What the tester may publish, and when | |
| Behaviour if the client disagrees with a finding | |

## Signatures

Tester: ______________________  Date: __________

Client: ______________________  Date: __________

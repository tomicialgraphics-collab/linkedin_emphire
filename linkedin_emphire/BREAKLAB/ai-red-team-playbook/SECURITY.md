# Responsible use

This repository is a testing methodology. It is meant to be used against systems you own, or systems you have written permission to test, under a signed scope of work.

## What is here

- A checklist of classes to test, with one sentence each describing the test and the evidence to keep.
- Tooling for counting results honestly: intervals, coverage arguments, validation.
- Templates for scope, findings and reports.

## What is not here

- Working exploits against named products.
- Payload strings aimed at a specific live system.
- Anything that turns a known bug into a weapon.

## If you find a vulnerability in someone else's system

Follow coordinated disclosure. Contact the vendor privately, give them a reasonable window, and agree the timeline before publishing. If they have no security contact, a public issue asking for one is usually acceptable and a public write up of the vulnerability is not.

## If you are testing under a contract

The stop condition in your rules of engagement outranks the checklist. If a test would touch a real customer, a live third party, or shared infrastructure, stop and ask. `templates/engagement-scope.md` exists so that this conversation happens before testing rather than after.

## Reporting a problem with this repository

Open an issue if the problem is in the writing or the tooling. If it is a security concern about how the material could be misused, describe it in general terms without including a working payload.

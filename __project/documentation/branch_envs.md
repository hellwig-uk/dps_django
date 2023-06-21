Branches and Environments
=========================

Environments are associated with a workflow branch.

main
----
This is the main working branch, the environment associated with it is `MAIN`
and has all the required dependencies including libraries for connecting to
external services and testing/qa packages. Prefixed working branches such as
`fix-` and `new-` are branched off from this. The dataset (if any) is generated.

live
----
This is the production branch, the environment associated with it is `LIVE`
which is equivalent to main except that testing/qa packages are omitted as well
as stubs for testing purposes for external services.

demo
----
This is the same as a production branch, however the dataset (if any) is 
generated. External services are also on their side sandboxed, if that is not
available using a demo account and if that is not possible a stub is used.

test
----
This is equivalent to main but the dataset (is any) is a anonymized version of
the live dataset.


Regional Variations
===================
For some organisations, the same code is deployed multiple times, in those cases
there should be a `default` regional variation for the automatic deployment.
For the `test` environment, each regional variation plus the `default` should
have a deployment.
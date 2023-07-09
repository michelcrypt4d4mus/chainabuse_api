Example `/reports` success response:
```json
[
  {
    "id": "52907745-7672-470e-a803-a2f8feb52944",
    "trusted": true,
    "checked": true,
    "scamCategory": "RUG_PULL",
    "createdAt": "2022-09-09T04:53:16.591Z",
    "addresses": [
      {
        "address": "12QeMLzSrB8XH8FvEzPMVoRxVAzTr5XM2y",
        "chain": "BTC",
        "domain": null
      },
      {
        "address": null,
        "chain": null,
        "domain": "scammer.com"
      }
    ]
  }
]
```


Example `/reports` failure response:
```json
{
  "reason": "string"
}
```

# Retraction Dashboard : backend

FastAPI backend for Retraction Dashboard

![rd-logo](./rd-logo.png)

## Tech Stack

**API Standards:** Open API 3.0.0

**Server:** FastAPI, NodeJS

## API Reference

#### Dummy API Reference

```http
  GET /api/data
```

| Parameter | Type     | Description                        |
| :-------- | :------- | :--------------------------------- |
| `api_key` | `string` | **Required**. Your API/Session key |

#### Get item

```http
  POST /api/items/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### add(num1, num2)

Takes two numbers and returns the sum.

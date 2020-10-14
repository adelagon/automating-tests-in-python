// index.js
module.exports = () => {
  const data = { users: [] }
  // Create 10 users
  for (let i = 0; i < 10; i++) {
    data.users.push({ id: i, name: `user${i}` })
  }
  return data
}
<template>
  <q-page>
    <div class="q-pa-md">
      <q-input
        outlined
        v-model="search"
        label="Search for a Player"
        @input="fetchPlayers"
      />
      <q-table
        :rows="players"
        :columns="columns"
        row-key="player_name"
        flat
      />
    </div>
  </q-page>
</template>

<script>
export default {
  data() {
    return {
      search: '',
      players: [],
      columns: [
        { name: 'player_name', label: 'Player Name', field: 'player_name', align: 'left' },
        { name: 'team', label: 'Team', field: 'team', align: 'center' },
        { name: 'avg', label: 'AVG', field: 'avg', align: 'center' },
      ],
    }
  },
  methods: {
    async fetchPlayers() {
      console.log('fetchPlayers triggered') // Debugging log
      try {
        const response = await this.$api.get('/players')
        console.log('API Response:', response.data) // Debugging log
        this.players = response.data
      } catch (error) {
        console.error('Error fetching players:', error)
      }
    },
  },
  mounted() {
    this.fetchPlayers() // Automatically fetch players on page load
  },
}
</script>

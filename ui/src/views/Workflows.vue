<template>
    <div class="kt-portlet kt-portlet--height-fluid">
        <div class="kt-portlet__head">
            <div class="kt-portlet__head-label">
                <h3 class="kt-portlet__head-title">
                    Available Workflows
                </h3>
            </div>
            <div class="kt-portlet__head-toolbar">
                <router-link :to="'/community/'+$route.params.community_id+'/workflow/create'"
                             class="btn btn-label-brand btn-bold btn-sm">
                    <i class="fa fa-plus-circle"></i> Create Workflow
                </router-link>
            </div>
        </div>
        <div class="kt-portlet__body kt-portlet__body--fluid">
            <b-row v-if="workflows.length > 0">
                <b-col cols="4" v-for="(workflow, i) in workflows" :key="workflow.id">
                    <workflow v-if="isMyCommunity || i === 0" :workflow="workflow"></workflow>
                </b-col>
            </b-row>
            <b-row v-else>
                <b-col>
                    <p class="text-black-50">There are no available workflows!</p>
                </b-col>
            </b-row>
        </div>
    </div>
</template>

<script>
    // @ is an alias to /src

    import Workflow from './Workflow.vue'
    import axios from 'axios'
    import store from '../store'

    export default {
        store: store,
        name: 'workflows',
        components: {
            Workflow
        },
        data() {
            return {
                community: [],
                workflows: [],
                isMyCommunity: false
            }
        },
        methods: {
            async getWorkflows(id = null) {
                try {
                    if (id === null)
                        id = this.$route.params.community_id

                    const {data} = await axios.get(process.env.VUE_APP_BASE_URL + 'community/' + id + '/workflow/', {
                        headers: {
                            Authorization: 'token ' + store.getters.token
                        }
                    })

                    if (data.length > 0)
                        return this.workflows = data
                } catch (e) {
                    if (e.response.status !== 500) {
                        Object.keys(e.response.data).forEach(key => {
                            this.$swal(key, e.response.data[key][0], 'error')
                        })
                    } else
                        this.$swal('Server Error!', e.message, 'error')
                }
            }
        },
        mounted() {
            this.getWorkflows()
        }
    }
</script>
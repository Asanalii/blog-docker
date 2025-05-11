<template>
  <div>
    <h2>📚 Blog Posts</h2>

    <form @submit.prevent="isEditing ? updatePost() : createPost()">
      <input v-model="newPost.title" placeholder="Title" required />
      <input v-model="newPost.content" placeholder="Content" required />
      <button type="submit">{{ isEditing ? "Update" : "Add" }} Post</button>
      <button v-if="isEditing" type="button" @click="cancelEdit">Cancel</button>
    </form>

    <ul>
      <li v-for="post in posts" :key="post.id">
        <strong>{{ post.title }}</strong
        >: {{ post.content }}
        <button @click="startEdit(post)">✏️ Edit</button>
        <button @click="deletePost(post.id)">🗑️ Delete</button>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";

const posts = ref([]);
const newPost = ref({ title: "", content: "" });
const isEditing = ref(false);
const editingPostId = ref(null);

const fetchPosts = async () => {
  const res = await axios.get("/api/posts");
  posts.value = res.data;
};

const createPost = async () => {
  await axios.post("/api/posts", newPost.value);
  resetForm();
  await fetchPosts();
};

const deletePost = async (id) => {
  await axios.delete(`/api/posts/${id}`);
  await fetchPosts();
};

const startEdit = (post) => {
  isEditing.value = true;
  editingPostId.value = post.id;
  newPost.value.title = post.title;
  newPost.value.content = post.content;
};

const cancelEdit = () => {
  resetForm();
};

const updatePost = async () => {
  await axios.put(`/api/posts/${editingPostId.value}`, newPost.value);
  resetForm();
  await fetchPosts();
};

const resetForm = () => {
  isEditing.value = false;
  editingPostId.value = null;
  newPost.value.title = "";
  newPost.value.content = "";
};

onMounted(fetchPosts);
</script>

/**
 * ProStory-AI - Composant racine React
 * Configure le routeur et la structure principale de l'application
 */

import React from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import { Navigation } from './components/Navigation'
import { HomePage } from './pages/HomePage'
import { ConnexionInscriptionPage } from './pages/ConnexionInscription'

export default function App() {
  return (
    <Router>
      <div className="min-h-screen bg-gray-50">
        <Navigation />
        <main>
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/connexion" element={<ConnexionInscriptionPage />} />
            <Route path="/inscription" element={<ConnexionInscriptionPage />} />
          </Routes>
        </main>
      </div>
    </Router>
  )
}

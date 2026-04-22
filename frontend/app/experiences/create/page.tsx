'use client'

import { useState } from 'react'
import { useRouter } from 'next/navigation'
import { Navigation } from '@/components/Navigation'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Card } from '@/components/ui/card'
import { Textarea } from '@/components/ui/textarea'
import { TagInput } from '@/components/TagInput'
import { RichTextEditor } from '@/components/RichTextEditor'
import { api } from '@/lib/api'

export default function CreateExperiencePage() {
  const router = useRouter()
  const [formData, setFormData] = useState({
    titre: '',
    contenu: '',
    tags: [] as string[],
    domaine_activite: ''
  })
  const [loading, setLoading] = useState(false)

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setLoading(true)
    try {
      const userId = localStorage.getItem('user_id')
      if (!userId) throw new Error('Utilisateur non connecté')

      const payload = {
        titre: formData.titre,
        contenu: formData.contenu,
        tags: formData.tags.join(', '),
        domaine_activite: formData.domaine_activite
      }

      await api.post('/api/experiences', payload, {
        headers: { 'x_user_id': userId }
      })
      router.push('/experiences')
    } catch (error) {
      console.error('Erreur création', error)
      alert('Erreur lors de la création')
    } finally {
      setLoading(false)
    }
  }

  return (
    <main className="min-h-screen bg-background">
      <Navigation />
      <div className="max-w-2xl mx-auto p-8">
        <Button variant="ghost" onClick={() => router.back()} className="mb-6">
          Annuler
        </Button>
        <Card className="p-8">
          <h1 className="text-3xl font-bold mb-8">Nouvelle Expérience</h1>
          <form onSubmit={handleSubmit} className="space-y-6">
            <div>
              <Label htmlFor="titre">Titre</Label>
              <Input
                id="titre"
                value={formData.titre}
                onChange={(e) => setFormData({...formData, titre: e.target.value})}
                placeholder="Titre de votre expérience"
                required
              />
            </div>

            <div>
              <Label htmlFor="contenu">Contenu</Label>
              <RichTextEditor
                value={formData.contenu}
                onChange={(value) => setFormData({...formData, contenu: value})}
                placeholder="Racontez votre expérience..."
              />
            </div>

            <div>
              <Label>Tags</Label>
              <TagInput
                value={formData.tags}
                onChange={(tags) => setFormData({...formData, tags})}
                placeholder="Ajoutez des tags (ex: #startup, #leadership)"
              />
            </div>

            <div>
              <Label htmlFor="domaine">Domaine d'activité</Label>
              <Input
                id="domaine"
                value={formData.domaine_activite}
                onChange={(e) => setFormData({...formData, domaine_activite: e.target.value})}
                placeholder="Ex: Tech, Marketing, Finance"
              />
            </div>

            <Button type="submit" className="w-full" disabled={loading}>
              {loading ? 'Création...' : 'Publier l\'expérience'}
            </Button>
          </form>
        </Card>
      </div>
    </main>
  )
}

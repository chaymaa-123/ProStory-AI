'use client'

import { useState } from 'react'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Textarea } from '@/components/ui/textarea'
import { X, Send } from 'lucide-react'
import { Dialog, DialogContent, DialogHeader, DialogTitle } from '@/components/ui/dialog'

interface QuickExperienceModalProps {
  open: boolean
  onOpenChange: (open: boolean) => void
  onSubmit?: (data: { title: string; content: string }) => void
}

export function QuickExperienceModal({
  open,
  onOpenChange,
  onSubmit,
}: QuickExperienceModalProps) {
  const [title, setTitle] = useState('')
  const [content, setContent] = useState('')
  const [isSubmitting, setIsSubmitting] = useState(false)

  const handleSubmit = async () => {
    if (!title.trim() || !content.trim()) return

    setIsSubmitting(true)
    await new Promise((resolve) => setTimeout(resolve, 300))

    onSubmit?.({
      title,
      content,
    })

    setTitle('')
    setContent('')
    setIsSubmitting(false)
    onOpenChange(false)
  }

  const charCount = content.length
  const maxChars = 280

  return (
    <Dialog open={open} onOpenChange={onOpenChange}>
      <DialogContent className="sm:max-w-[500px] p-0 overflow-hidden">
        <DialogHeader className="px-6 py-4 border-b border-border">
          <DialogTitle>Partage une expérience</DialogTitle>
        </DialogHeader>

        <div className="p-6 space-y-4">
          {/* Title */}
          <div>
            <Input
              placeholder="Titre de ton expérience"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              className="rounded-lg font-medium text-base"
              maxLength={100}
            />
            <p className="text-xs text-muted-foreground mt-1">
              {title.length}/100 caractères
            </p>
          </div>

          {/* Content */}
          <div>
            <Textarea
              placeholder="Raconte ton histoire... (rapide et simple !)"
              value={content}
              onChange={(e) => setContent(e.target.value)}
              maxLength={maxChars}
              rows={5}
              className="rounded-lg resize-none"
            />
            <p className="text-xs text-muted-foreground mt-1">
              {charCount}/{maxChars} caractères
            </p>
          </div>

          {/* Actions */}
          <div className="flex gap-3 pt-2">
            <Button
              variant="outline"
              className="flex-1 rounded-lg"
              onClick={() => onOpenChange(false)}
            >
              Annuler
            </Button>
            <Button
              className="flex-1 rounded-lg"
              disabled={!title.trim() || !content.trim() || isSubmitting}
              onClick={handleSubmit}
            >
              {isSubmitting ? (
                'Partage...'
              ) : (
                <>
                  <Send className="w-4 h-4 mr-2" />
                  Partager
                </>
              )}
            </Button>
          </div>
        </div>
      </DialogContent>
    </Dialog>
  )
}
